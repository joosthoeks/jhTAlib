""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def AEX_BEURSCYCLUS(df, n=252, price='Close'):
    """
    AEX Beurscyclus - Amsterdam stock-exchange cycle-phase classifier (beurscyclus.nl AEXcel model).

    Classifies each bar of an AEX-like price series into one of the four classic cycle
    phases - accumulation (0), markup (1), distribution (2), markdown (3) - using the
    (Grand)Cycle level of the AEXcel model of beurscyclus.nl.

    Theory: The AEXcel model tracks a nested hierarchy of Dutch equity-market cycles.
            Expressed in Euronext trading days at the ~21-trading-days-per-month
            convention the levels are:
              - Minute cycle:            1-3 weeks   (~5-15 trading days)
              - Minor cycle:             3-5 weeks   (~15-25 trading days)
              - Primary cycle:           3-4 months  (~63-84 trading days, ~74 at midpoint)
              - (Grand)Cycle:            7-9 months  (~147-189 trading days, 168 at midpoint)
              - Kitchin/business cycle:  ~53 months  (~1113 trading days) average on AEX data since 1994
            Because 53 months / 8 months = 1113 / 168 ~= 6.6, one Kitchin cycle spans
            roughly six to seven (Grand)Cycles: it is several times longer than a single
            (Grand)Cycle, not the "4x the GrandCycle" small-integer multiple sometimes
            quoted as a rule of thumb. (The individual
            day/month figures are consistent at 21 trading days per month: 74 ~= 3.5 x 21,
            168 = 8 x 21, 1113 = 53 x 21.)
            This function operates at the (Grand)Cycle level. For each bar it takes a
            rolling window of n bars and locates the current price within that window's
            high-low range (norm_pos: 0 = at the window low, 1 = at the window high) as a
            price-only proxy for the model's lowest-low / oscillator trough location. It
            then maps the four range quarters onto the four cycle phases, resolving the
            two middle quarters by whether price is above or below the window's first bar:
              norm_pos < 0.25                     -> accumulation (0)
              0.25 <= norm_pos < 0.50             -> markup (1) if rising, else accumulation (0)
              0.50 <= norm_pos < 0.75             -> distribution (2) if rising, else markup (1)
              norm_pos >= 0.75, price rising       -> distribution (2)
              norm_pos >= 0.75, price falling      -> markdown (3)
            cycle_strength scores how consistently the most recent ~1 Minor cycle
            (the last 20 bars ~ 4 weeks) moves in the assigned phase direction, on 0-1.
            next_turning_point estimates the trading days to the next phase change from
            (Grand)Cycle geometry: the accumulation and distribution quarters are the
            shorter turns (grand_cycle // 4 = 42 bars), the markup and markdown legs the
            longer halves (grand_cycle // 2 = 84 bars).
            n=252 (~one Euronext trading year) is chosen so every window spans at least one
            complete (Grand)Cycle (147-189 trading days) with margin.

    Returns: dict with lists
             'cycle_phase'        (0=accumulation, 1=markup, 2=distribution, 3=markdown),
             'cycle_strength'     (phase-direction consistency, 0-1),
             'next_turning_point' (estimated trading days to next phase change),
             each NaN during the n-1 bar warm-up
             = jhta.AEX_BEURSCYCLUS(df, n=252, price='Close')
    Source: https://beurscyclus.nl/aexcycli (AEXcel model, cycle hierarchy)
    """
    cycle_phase = []
    cycle_strength = []
    next_turning_point = []

    # AEXcel "(Grand)Cycle" of 7-9 months, midpoint 8 months x ~21 trading days/month;
    # its quarters (grand_cycle // 4) and halves (grand_cycle // 2) drive the
    # turning-point estimates below.
    grand_cycle = 168

    for i in range(len(df[price])):
        if i + 1 < n:
            cycle_phase.append(float('NaN'))
            cycle_strength.append(float('NaN'))
            next_turning_point.append(float('NaN'))
            continue

        # Window of n bars (default one Euronext trading year, >= one full (Grand)Cycle)
        start = i + 1 - n
        end = i + 1
        window = df[price][start:end]

        # Position of the current price within the rolling window range
        # (0 = at window low, 1 = at window high): a price-only proxy for the
        # AEXcel lowest-low / oscillator trough location.
        low = min(window)
        high = max(window)
        current = window[-1]
        first = window[0]
        price_range = high - low
        if price_range > 0:
            norm_pos = (current - low) / price_range
        else:
            norm_pos = 0.5

        # Map the four range quarters onto the four (Grand)Cycle phases:
        # 0 = accumulation (near cycle low), 1 = markup, 2 = distribution (near cycle
        # high), 3 = markdown. The two middle quarters are resolved by trend direction.
        if norm_pos < 0.25:
            phase = 0
        elif norm_pos < 0.5:
            phase = 1 if current > first else 0
        elif norm_pos < 0.75:
            phase = 2 if current > first else 1
        else:
            phase = 2
        if norm_pos > 0.75 and current < first:
            phase = 3

        # Cycle strength: consistency of the last ~1 Minor cycle (20 bars ~ 4 weeks,
        # within the AEXcel Minor range of 3-5 weeks) with the assigned phase direction.
        recent_bars = window[-20:] if len(window) >= 20 else window
        trend_consistent = 0
        for j in range(len(recent_bars) - 1):
            if (recent_bars[j + 1] > recent_bars[j] and phase in [1, 2]) or \
               (recent_bars[j + 1] < recent_bars[j] and phase == 3):
                trend_consistent += 1
        if len(recent_bars) > 1:
            strength = trend_consistent / (len(recent_bars) - 1)
        else:
            strength = 0.5

        # Next turning point from (Grand)Cycle structure (168 days ~ 8 months):
        # accumulation/distribution are the shorter transition quarters (grand_cycle // 4
        # = 42 bars), markup/markdown the longer halves (grand_cycle // 2 = 84 bars).
        if phase == 0:
            turning_bars = grand_cycle // 4
        elif phase == 1:
            turning_bars = grand_cycle // 2
        elif phase == 2:
            turning_bars = grand_cycle // 4
        else:
            turning_bars = grand_cycle // 2

        cycle_phase.append(phase)
        cycle_strength.append(strength)
        next_turning_point.append(turning_bars)

    return {'cycle_phase': cycle_phase, 'cycle_strength': cycle_strength, 'next_turning_point': next_turning_point}
