""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def ANOVA_ONE_WAY(groups):
    """
    One-Way ANOVA - F-test comparing the means of two or more groups of price returns
    Theory: the total variation of all observations is split into variation between the group
            means and variation within each group. With k groups and N total observations:
            SSB = sum(n_i * (mean_i - grand_mean)^2), SSW = sum over groups of sum((x - mean_i)^2),
            df_between = k - 1, df_within = N - k, and F = (SSB / df_between) / (SSW / df_within).
            A large F means the group means differ more than chance alone would explain; F near 0
            means the groups have essentially the same mean. In simple terms: it checks whether
            several sets of returns (for example returns from different weekdays or regimes)
            really behave differently on average, or only appear to. Groups with identical means
            give F = 0; if all groups are internally constant but their means differ, F is
            infinite. groups must contain at least 2 groups and N - k must be at least 1.
    Returns: dict = jhta.ANOVA_ONE_WAY(groups)
            {'f_statistic': float, 'df_between': int, 'df_within': int}
    Source: Fisher, R. A. (1925). Statistical Methods for Research Workers. Oliver and Boyd.
    """
    k = len(groups)
    counts = [len(group) for group in groups]
    total_n = sum(counts)
    df_between = k - 1
    df_within = total_n - k
    if k < 2 or min(counts) < 1 or df_within < 1:
        return {
            'f_statistic': float('NaN'),
            'df_between': df_between,
            'df_within': df_within
            }
    grand_mean = sum(sum(group) for group in groups) / float(total_n)
    ss_between = 0.0
    ss_within = 0.0
    for group in groups:
        group_mean = sum(group) / float(len(group))
        diff = group_mean - grand_mean
        ss_between += len(group) * diff * diff
        for x in group:
            dev = x - group_mean
            ss_within += dev * dev
    ms_between = ss_between / float(df_between)
    ms_within = ss_within / float(df_within)
    if ms_within == 0.0:
        f_statistic = 0.0 if ms_between == 0.0 else float('inf')
    else:
        f_statistic = ms_between / ms_within
    return {
        'f_statistic': f_statistic,
        'df_between': df_between,
        'df_within': df_within
        }
