=======
jhTAlib
=======

:Author: Joost Hoeks
:Date:   2019-03-08

.. contents::
   :depth: 3
..

jhTAlib
=======

Technical Analysis Library Time-Series

You can use and import it for your:

-  Technical Analysis Software

-  Charting Software

-  Backtest Software

-  Trading Robot Software

-  Trading Software in general

Work in progress...

Depends only on
---------------

-  `The Python Standard
   Library <https://docs.python.org/3/library/index.html>`__

Install
-------

From `PyPI <https://pypi.org/project/jhTAlib/>`__:

::

    $ [sudo] pip3 install jhtalib

From `source <https://github.com/joosthoeks/jhTAlib>`__:

::

    $ git clone https://github.com/joosthoeks/jhTAlib.git
    $ cd jhTAlib
    $ [sudo] pip3 install -e .

Update
------

From `PyPI <https://pypi.org/project/jhTAlib/>`__:

::

    $ [sudo] pip3 install --upgrade jhtalib

From `source <https://github.com/joosthoeks/jhTAlib>`__:

::

    $ cd jhTAlib
    $ git pull [upstream master]

Examples
--------

::

    $ cd example/

Example 1
~~~~~~~~~

::

    $ python3 example-1-plot.py

or

|Open In Colab|

Example 2
~~~~~~~~~

::

    $ python3 example-2-plot.py

or

|Open In Colab|

Example 3
~~~~~~~~~

::

    $ python3 example-3-plot.py

or

|Open In Colab|

Example 4
~~~~~~~~~

::

    $ python3 example-4-plot-quandl.py

or

|Open In Colab|

Example 5
~~~~~~~~~

::

    $ python3 example-5-plot-quandl.py

or

|Open In Colab|

Example 6
~~~~~~~~~

::

    $ python3 example-6-plot-quandl.py

or

|Open In Colab|

Example 7
~~~~~~~~~

::

    $ python3 example-7-quandl-2-df.py

or

|Open In Colab|

Example 8
~~~~~~~~~

::

    $ python3 example-8-alphavantage-2-df.py

or

|Open In Colab|

Example 9
~~~~~~~~~

::

    $ python3 example-9-cryptocompare-2-df.py

or

|Open In Colab|

Example 10
~~~~~~~~~~

DF NumPy Pandas

|Open In Colab|

Test
----

::

    $ cd test/
    $ python3 test.py

Reference
---------

::

    import jhtalib as jhta

+------+------+------+
| Indi | Name | TODO |
| cato | /    |      |
| r    | Para |      |
| /    | ms   |      |
| Retu |      |      |
| rns  |      |      |
+======+======+======+
| **`b |      |
| ehav |      |
| iora |      |
| l\_t |      |
| echn |      |
| ique |      |
| s <h |      |
| ttps |      |
| ://g |      |
| ithu |      |
| b.co |      |
| m/jo |      |
| osth |      |
| oeks |      |
| /jhT |      |
| Alib |      |
| /blo |      |
| b/ma |      |
| ster |      |
| /jht |      |
| alib |      |
| /beh |      |
| avio |      |
| ral_ |      |
| tech |      |
| niqu |      |
| es/b |      |
| ehav |      |
| iora |      |
| l_te |      |
| chni |      |
| ques |      |
| .py> |      |
| `__* |      |
| *    |      |
+------+------+------+
| ATH  | All  | DONE |
|      | Time |      |
|      | High |      |
+------+------+------+
| dict | ``jh |
| of   | ta.A |
| list | TH(d |
| s    | f, p |
|      | rice |
|      | ='Hi |
|      | gh') |
|      | ``   |
+------+------+------+
| LMC  | Last | DONE |
|      | Majo |      |
|      | r    |      |
|      | Corr |      |
|      | ecti |      |
|      | on   |      |
+------+------+------+
| dict | ``jh |
| of   | ta.L |
| list | MC(d |
| s    | f, p |
|      | rice |
|      | ='Lo |
|      | w')` |
|      | `    |
+------+------+------+
| PP   | Pivo | DONE |
|      | t    |      |
|      | Poin |      |
|      | t    |      |
+------+------+------+
| dict | ``jh |
| of   | ta.P |
| list | P(df |
| s    | )``  |
+------+------+------+
| FIBO | Fibo | DONE |
| PR   | nacc |      |
|      | i    |      |
|      | Pric |      |
|      | e    |      |
|      | Retr |      |
|      | acem |      |
|      | ents |      |
+------+------+------+
| dict | ``jh |
| of   | ta.F |
| list | IBOP |
| s    | R(df |
|      | , pr |
|      | ice= |
|      | 'Clo |
|      | se') |
|      | ``   |
+------+------+------+
| FIBO | Fibo |
| TR   | nacc |
|      | i    |
|      | Time |
|      | Retr |
|      | acem |
|      | ents |
+------+------+------+
| GANN | W.   | DONE |
| PR   | D.   |      |
|      | Gann |      |
|      | Pric |      |
|      | e    |      |
|      | Retr |      |
|      | acem |      |
|      | ents |      |
+------+------+------+
| dict | ``jh |
| of   | ta.G |
| list | ANNP |
| s    | R(df |
|      | , pr |
|      | ice= |
|      | 'Clo |
|      | se') |
|      | ``   |
+------+------+------+
| GANN | W.   |
| TR   | D.   |
|      | Gann |
|      | Time |
|      | Retr |
|      | acem |
|      | ents |
+------+------+------+
| JDN  | Juli | DONE |
|      | an   |      |
|      | Day  |      |
|      | Numb |      |
|      | er   |      |
+------+------+------+
| jdn  | ``jh |
|      | ta.J |
|      | DN(u |
|      | tc_y |
|      | ear, |
|      |  utc |
|      | _mon |
|      | th,  |
|      | utc_ |
|      | day) |
|      | ``   |
+------+------+------+
| JD   | Juli | DONE |
|      | an   |      |
|      | Date |      |
+------+------+------+
| jd   | ``jh |
|      | ta.J |
|      | D(ut |
|      | c_ye |
|      | ar,  |
|      | utc_ |
|      | mont |
|      | h, u |
|      | tc_d |
|      | ay,  |
|      | utc_ |
|      | hour |
|      | , ut |
|      | c_mi |
|      | nute |
|      | , ut |
|      | c_se |
|      | cond |
|      | )``  |
+------+------+------+
| SUNC | Sun  |
|      | Cycl |
|      | e    |
+------+------+------+
| MERC | Merc |
| URYC | ury  |
|      | Cycl |
|      | e    |
+------+------+------+
| VENU | Venu |
| SC   | s    |
|      | Cycl |
|      | e    |
+------+------+------+
| EART | Eart |
| HC   | h    |
|      | Cycl |
|      | e    |
+------+------+------+
| MARS | Mars |
| C    | Cycl |
|      | e    |
+------+------+------+
| JUPI | Jupi |
| TERC | ter  |
|      | Cycl |
|      | e    |
+------+------+------+
| SATU | Satu |
| RNC  | rn   |
|      | Cycl |
|      | e    |
+------+------+------+
| URAN | Uran |
| USC  | us   |
|      | Cycl |
|      | e    |
+------+------+------+
| NEPT | Nept |
| UNEC | une  |
|      | Cycl |
|      | e    |
+------+------+------+
| PLUT | Plut |
| OC   | o    |
|      | Cycl |
|      | e    |
+------+------+------+
| MOON | Moon |
| C    | Cycl |
|      | e    |
+------+------+------+
| **`c |      |
| ycle |      |
| \_in |      |
| dica |      |
| tors |      |
|  <ht |      |
| tps: |      |
| //gi |      |
| thub |      |
| .com |      |
| /joo |      |
| stho |      |
| eks/ |      |
| jhTA |      |
| lib/ |      |
| blob |      |
| /mas |      |
| ter/ |      |
| jhta |      |
| lib/ |      |
| cycl |      |
| e_in |      |
| dica |      |
| tors |      |
| /cyc |      |
| le_i |      |
| ndic |      |
| ator |      |
| s.py |      |
| >`__ |      |
| **   |      |
+------+------+------+
| HT\_ | Hilb |
| DCPE | ert  |
| RIOD | Tran |
|      | sfor |
|      | m    |
|      | -    |
|      | Domi |
|      | nant |
|      | Cycl |
|      | e    |
|      | Peri |
|      | od   |
+------+------+------+
| HT\_ | Hilb |
| DCPH | ert  |
| ASE  | Tran |
|      | sfor |
|      | m    |
|      | -    |
|      | Domi |
|      | nant |
|      | Cycl |
|      | e    |
|      | Phas |
|      | e    |
+------+------+------+
| HT\_ | Hilb |
| PHAS | ert  |
| OR   | Tran |
|      | sfor |
|      | m    |
|      | -    |
|      | Phas |
|      | or   |
|      | Comp |
|      | onen |
|      | ts   |
+------+------+------+
| HT\_ | Hilb |
| SINE | ert  |
|      | Tran |
|      | sfor |
|      | m    |
|      | -    |
|      | Sine |
|      | Wave |
+------+------+------+
| HT\_ | Hilb |
| TREN | ert  |
| DLIN | Tran |
| E    | sfor |
|      | m    |
|      | -    |
|      | Inst |
|      | anta |
|      | neou |
|      | s    |
|      | Tren |
|      | dlin |
|      | e    |
+------+------+------+
| HT\_ | Hilb |
| TREN | ert  |
| DMOD | Tran |
| E    | sfor |
|      | m    |
|      | -    |
|      | Tren |
|      | d    |
|      | vs   |
|      | Cycl |
|      | e    |
|      | Mode |
+------+------+------+
| TS   | Tren | DONE |
|      | d    |      |
|      | Scor |      |
|      | e    |      |
+------+------+------+
| list | ``jh |
|      | ta.T |
|      | S(df |
|      | , n, |
|      |  pri |
|      | ce=' |
|      | Clos |
|      | e')` |
|      | `    |
+------+------+------+
| **`d |      |
| ata  |      |
| <htt |      |
| ps:/ |      |
| /git |      |
| hub. |      |
| com/ |      |
| joos |      |
| thoe |      |
| ks/j |      |
| hTAl |      |
| ib/b |      |
| lob/ |      |
| mast |      |
| er/j |      |
| htal |      |
| ib/d |      |
| ata/ |      |
| data |      |
| .py> |      |
| `__* |      |
| *    |      |
+------+------+------+
| CSV2 | CSV  | DONE |
| DF   | file |      |
|      | 2    |      |
|      | Data |      |
|      | Feed |      |
+------+------+------+
| dict | ``jh |
| of   | ta.C |
| tupl | SV2D |
| es   | F(cs |
|      | v_fi |
|      | le_p |
|      | ath) |
|      | ``   |
+------+------+------+
| CSVU | CSV  | DONE |
| RL2D | file |      |
| F    | url  |      |
|      | 2    |      |
|      | Data |      |
|      | Feed |      |
+------+------+------+
| dict | ``jh |
| of   | ta.C |
| tupl | SVUR |
| es   | L2DF |
|      | (csv |
|      | _fil |
|      | e_ur |
|      | l)`` |
+------+------+------+
| DF2C | Data | DONE |
| SV   | Feed |      |
|      | 2    |      |
|      | CSV  |      |
|      | file |      |
+------+------+------+
| csv  | ``jh |
| file | ta.D |
|      | F2CS |
|      | V(df |
|      | , cs |
|      | v_fi |
|      | le_p |
|      | ath) |
|      | ``   |
+------+------+------+
| DF2D | Data | DONE |
| FREV | Feed |      |
|      | 2    |      |
|      | Data |      |
|      | Feed |      |
|      | Reve |      |
|      | rsed |      |
+------+------+------+
| dict | ``jh |
| of   | ta.D |
| tupl | F2DF |
| es   | REV( |
|      | df)` |
|      | `    |
+------+------+------+
| DF2D | Data | DONE |
| FWIN | Feed |      |
|      | 2    |      |
|      | Data |      |
|      | Feed |      |
|      | Wind |      |
|      | ow   |      |
+------+------+------+
| dict | ``jh |
| of   | ta.D |
| tupl | F2DF |
| es   | WIN( |
|      | df,  |
|      | star |
|      | t=0, |
|      |  end |
|      | =10) |
|      | ``   |
+------+------+------+
| DF\_ | Data | DONE |
| HEAD | Feed |      |
|      | HEAD |      |
+------+------+------+
| dict | ``jh |
| of   | ta.D |
| tupl | F_HE |
| es   | AD(d |
|      | f, n |
|      | =5)` |
|      | `    |
+------+------+------+
| DF\_ | Data | DONE |
| TAIL | Feed |      |
|      | TAIL |      |
+------+------+------+
| dict | ``jh |
| of   | ta.D |
| tupl | F_TA |
| es   | IL(d |
|      | f, n |
|      | =5)` |
|      | `    |
+------+------+------+
| DF2H | Data | DONE |
| EIKI | Feed |      |
| N\_A | 2    |      |
| SHI  | Heik |      |
|      | in-A |      |
|      | shi  |      |
|      | Data |      |
|      | Feed |      |
+------+------+------+
| dict | ``jh |
| of   | ta.D |
| tupl | F2HE |
| es   | IKIN |
|      | _ASH |
|      | I(df |
|      | )``  |
+------+------+------+
| **`e |      |
| vent |      |
| \_dr |      |
| iven |      |
|  <ht |      |
| tps: |      |
| //gi |      |
| thub |      |
| .com |      |
| /joo |      |
| stho |      |
| eks/ |      |
| jhTA |      |
| lib/ |      |
| blob |      |
| /mas |      |
| ter/ |      |
| jhta |      |
| lib/ |      |
| even |      |
| t_dr |      |
| iven |      |
| /eve |      |
| nt_d |      |
| rive |      |
| n.py |      |
| >`__ |      |
| **   |      |
+------+------+------+
| ASI  | Accu | DONE |
|      | mula |      |
|      | tion |      |
|      | Swin |      |
|      | g    |      |
|      | Inde |      |
|      | x    |      |
|      | (J.  |      |
|      | Well |      |
|      | es   |      |
|      | Wild |      |
|      | er)  |      |
+------+------+------+
| list | ``jh |
|      | ta.A |
|      | SI(d |
|      | f, L |
|      | )``  |
+------+------+------+
| SI   | Swin | DONE |
|      | g    |      |
|      | Inde |      |
|      | x    |      |
|      | (J.  |      |
|      | Well |      |
|      | es   |      |
|      | Wild |      |
|      | er)  |      |
+------+------+------+
| list | ``jh |
|      | ta.S |
|      | I(df |
|      | , L) |
|      | ``   |
+------+------+------+
| **`e |      |
| xper |      |
| imen |      |
| tal  |      |
| <htt |      |
| ps:/ |      |
| /git |      |
| hub. |      |
| com/ |      |
| joos |      |
| thoe |      |
| ks/j |      |
| hTAl |      |
| ib/b |      |
| lob/ |      |
| mast |      |
| er/j |      |
| htal |      |
| ib/e |      |
| xper |      |
| imen |      |
| tal/ |      |
| expe |      |
| rime |      |
| ntal |      |
| .py> |      |
| `__* |      |
| *    |      |
+------+------+------+
| JH\_ | Swin | DONE |
| SAVG | g    |      |
| P    | Aver |      |
|      | age  |      |
|      | Pric |      |
|      | e    |      |
|      | -    |      |
|      | prev |      |
|      | ious |      |
|      | Aver |      |
|      | age  |      |
|      | Pric |      |
|      | e    |      |
+------+------+------+
| list | ``jh |
|      | ta.J |
|      | H_SA |
|      | VGP( |
|      | df)` |
|      | `    |
+------+------+------+
| JH\_ | Swin | DONE |
| SAVG | g    |      |
| PS   | Aver |      |
|      | age  |      |
|      | Pric |      |
|      | e    |      |
|      | -    |      |
|      | prev |      |
|      | ious |      |
|      | Aver |      |
|      | age  |      |
|      | Pric |      |
|      | e    |      |
|      | Summ |      |
|      | atio |      |
|      | n    |      |
+------+------+------+
| list | ``jh |
|      | ta.J |
|      | H_SA |
|      | VGPS |
|      | (df) |
|      | ``   |
+------+------+------+
| JH\_ | Swin | DONE |
| SCO  | g    |      |
|      | Clos |      |
|      | e    |      |
|      | -    |      |
|      | Open |      |
+------+------+------+
| list | ``jh |
|      | ta.J |
|      | H_SC |
|      | O(df |
|      | )``  |
+------+------+------+
| JH\_ | Swin | DONE |
| SCOS | g    |      |
|      | Clos |      |
|      | e    |      |
|      | -    |      |
|      | Open |      |
|      | Summ |      |
|      | atio |      |
|      | n    |      |
+------+------+------+
| list | ``jh |
|      | ta.J |
|      | H_SC |
|      | OS(d |
|      | f)`` |
+------+------+------+
| JH\_ | Swin | DONE |
| SMED | g    |      |
| P    | Medi |      |
|      | an   |      |
|      | Pric |      |
|      | e    |      |
|      | -    |      |
|      | prev |      |
|      | ious |      |
|      | Medi |      |
|      | an   |      |
|      | Pric |      |
|      | e    |      |
+------+------+------+
| list | ``jh |
|      | ta.J |
|      | H_SM |
|      | EDP( |
|      | df)` |
|      | `    |
+------+------+------+
| JH\_ | Swin | DONE |
| SMED | g    |      |
| PS   | Medi |      |
|      | an   |      |
|      | Pric |      |
|      | e    |      |
|      | -    |      |
|      | prev |      |
|      | ious |      |
|      | Medi |      |
|      | an   |      |
|      | Pric |      |
|      | e    |      |
|      | Summ |      |
|      | atio |      |
|      | n    |      |
+------+------+------+
| list | ``jh |
|      | ta.J |
|      | H_SM |
|      | EDPS |
|      | (df) |
|      | ``   |
+------+------+------+
| JH\_ | Swin | DONE |
| SPP  | g    |      |
|      | Pric |      |
|      | e    |      |
|      | -    |      |
|      | prev |      |
|      | ious |      |
|      | Pric |      |
|      | e    |      |
+------+------+------+
| list | ``jh |
|      | ta.J |
|      | H_SP |
|      | P(df |
|      | , pr |
|      | ice= |
|      | 'Clo |
|      | se') |
|      | ``   |
+------+------+------+
| JH\_ | Swin | DONE |
| SPPS | g    |      |
|      | Pric |      |
|      | e    |      |
|      | -    |      |
|      | prev |      |
|      | ious |      |
|      | Pric |      |
|      | e    |      |
|      | Summ |      |
|      | atio |      |
|      | n    |      |
+------+------+------+
| list | ``jh |
|      | ta.J |
|      | H_SP |
|      | PS(d |
|      | f, p |
|      | rice |
|      | ='Cl |
|      | ose' |
|      | )``  |
+------+------+------+
| JH\_ | Swin | DONE |
| STYP | g    |      |
| P    | Typi |      |
|      | cal  |      |
|      | Pric |      |
|      | e    |      |
|      | -    |      |
|      | prev |      |
|      | ious |      |
|      | Typi |      |
|      | cal  |      |
|      | Pric |      |
|      | e    |      |
+------+------+------+
| list | ``jh |
|      | ta.J |
|      | H_ST |
|      | YPP( |
|      | df)` |
|      | `    |
+------+------+------+
| JH\_ | Swin | DONE |
| STYP | g    |      |
| PS   | Typi |      |
|      | cal  |      |
|      | Pric |      |
|      | e    |      |
|      | -    |      |
|      | prev |      |
|      | ious |      |
|      | Typi |      |
|      | cal  |      |
|      | Pric |      |
|      | e    |      |
|      | Summ |      |
|      | atio |      |
|      | n    |      |
+------+------+------+
| list | ``jh |
|      | ta.J |
|      | H_ST |
|      | YPPS |
|      | (df) |
|      | ``   |
+------+------+------+
| JH\_ | Swin | DONE |
| SWCL | g    |      |
| P    | Weig |      |
|      | hted |      |
|      | Clos |      |
|      | e    |      |
|      | Pric |      |
|      | e    |      |
|      | -    |      |
|      | prev |      |
|      | ious |      |
|      | Weig |      |
|      | hted |      |
|      | Clos |      |
|      | e    |      |
|      | Pric |      |
|      | e    |      |
+------+------+------+
| list | ``jh |
|      | ta.J |
|      | H_SW |
|      | CLP( |
|      | df)` |
|      | `    |
+------+------+------+
| JH\_ | Swin | DONE |
| SWCL | g    |      |
| PS   | Weig |      |
|      | hted |      |
|      | Clos |      |
|      | e    |      |
|      | Pric |      |
|      | e    |      |
|      | -    |      |
|      | prev |      |
|      | ious |      |
|      | Weig |      |
|      | hted |      |
|      | Clos |      |
|      | e    |      |
|      | Pric |      |
|      | e    |      |
|      | Summ |      |
|      | atio |      |
|      | n    |      |
+------+------+------+
| list | ``jh |
|      | ta.J |
|      | H_SW |
|      | CLPS |
|      | (df) |
|      | ``   |
+------+------+------+
| **`g |      |
| ener |      |
| al < |      |
| http |      |
| s:// |      |
| gith |      |
| ub.c |      |
| om/j |      |
| oost |      |
| hoek |      |
| s/jh |      |
| TAli |      |
| b/bl |      |
| ob/m |      |
| aste |      |
| r/jh |      |
| tali |      |
| b/ge |      |
| nera |      |
| l/ge |      |
| nera |      |
| l.py |      |
| >`__ |      |
| **   |      |
+------+------+------+
| NORM | Norm | DONE |
| ALIZ | aliz |      |
| E    | e    |      |
+------+------+------+
| list | ``jh |
|      | ta.N |
|      | ORMA |
|      | LIZE |
|      | (df, |
|      |  pri |
|      | ce_m |
|      | ax=' |
|      | High |
|      | ', p |
|      | rice |
|      | _min |
|      | ='Lo |
|      | w',  |
|      | pric |
|      | e='C |
|      | lose |
|      | ')`` |
+------+------+------+
| STAN | Stan | DONE |
| DARD | dard |      |
| IZE  | ize  |      |
+------+------+------+
| list | ``jh |
|      | ta.S |
|      | TAND |
|      | ARDI |
|      | ZE(d |
|      | f, p |
|      | rice |
|      | ='Cl |
|      | ose' |
|      | )``  |
+------+------+------+
| SPRE | Spre | DONE |
| AD   | ad   |      |
+------+------+------+
| list | ``jh |
|      | ta.S |
|      | PREA |
|      | D(df |
|      | 1, d |
|      | f2,  |
|      | pric |
|      | e1=' |
|      | Clos |
|      | e',  |
|      | pric |
|      | e2=' |
|      | Clos |
|      | e')` |
|      | `    |
+------+------+------+
| CP   | Comp | DONE |
|      | arat |      |
|      | ive  |      |
|      | Perf |      |
|      | orma |      |
|      | nce  |      |
+------+------+------+
| list | ``jh |
|      | ta.C |
|      | P(df |
|      | 1, d |
|      | f2,  |
|      | pric |
|      | e1=' |
|      | Clos |
|      | e',  |
|      | pric |
|      | e2=' |
|      | Clos |
|      | e')` |
|      | `    |
+------+------+------+
| CRSI | Comp | DONE |
|      | arat |      |
|      | ive  |      |
|      | Rela |      |
|      | tive |      |
|      | Stre |      |
|      | ngth |      |
|      | Inde |      |
|      | x    |      |
+------+------+------+
| list | ``jh |
|      | ta.C |
|      | RSI( |
|      | df1, |
|      |  df2 |
|      | , n, |
|      |  pri |
|      | ce1= |
|      | 'Clo |
|      | se', |
|      |  pri |
|      | ce2= |
|      | 'Clo |
|      | se') |
|      | ``   |
+------+------+------+
| CS   | Comp | DONE |
|      | arat |      |
|      | ive  |      |
|      | Stre |      |
|      | ngth |      |
+------+------+------+
| list | ``jh |
|      | ta.C |
|      | S(df |
|      | 1, d |
|      | f2,  |
|      | pric |
|      | e1=' |
|      | Clos |
|      | e',  |
|      | pric |
|      | e2=' |
|      | Clos |
|      | e')` |
|      | `    |
+------+------+------+
| HR   | Hit  | DONE |
|      | Rate |      |
|      | /    |      |
|      | Win  |      |
|      | Rate |      |
+------+------+------+
| floa | ``jh |
| t    | ta.H |
|      | R(hi |
|      | t_tr |
|      | ades |
|      | _int |
|      | , to |
|      | tal_ |
|      | trad |
|      | es_i |
|      | nt)` |
|      | `    |
+------+------+------+
| PLR  | Prof | DONE |
|      | it/L |      |
|      | oss  |      |
|      | Rati |      |
|      | o    |      |
+------+------+------+
| floa | ``jh |
| t    | ta.P |
|      | LR(m |
|      | ean_ |
|      | trad |
|      | e_pr |
|      | ofit |
|      | _flo |
|      | at,  |
|      | mean |
|      | _tra |
|      | de_l |
|      | oss_ |
|      | floa |
|      | t)`` |
+------+------+------+
| EV   | Expe | DONE |
|      | cted |      |
|      | Valu |      |
|      | e    |      |
+------+------+------+
| floa | ``jh |
| t    | ta.E |
|      | V(hi |
|      | trad |
|      | e_fl |
|      | oat, |
|      |  mea |
|      | n_tr |
|      | ade_ |
|      | prof |
|      | it_f |
|      | loat |
|      | , me |
|      | an_t |
|      | rade |
|      | _los |
|      | s_fl |
|      | oat) |
|      | ``   |
+------+------+------+
| POR  | Prob | DONE |
|      | abil |      |
|      | ity  |      |
|      | of   |      |
|      | Ruin |      |
|      | (Tab |      |
|      | le   |      |
|      | of   |      |
|      | Luca |      |
|      | s    |      |
|      | and  |      |
|      | LeBe |      |
|      | au)  |      |
+------+------+------+
| int  | ``jh |
|      | ta.P |
|      | OR(h |
|      | itra |
|      | de_f |
|      | loat |
|      | , pr |
|      | ofit |
|      | _los |
|      | s_ra |
|      | tio_ |
|      | floa |
|      | t)`` |
+------+------+------+
| **`i |      |
| nfor |      |
| mati |      |
| on < |      |
| http |      |
| s:// |      |
| gith |      |
| ub.c |      |
| om/j |      |
| oost |      |
| hoek |      |
| s/jh |      |
| TAli |      |
| b/bl |      |
| ob/m |      |
| aste |      |
| r/jh |      |
| tali |      |
| b/in |      |
| form |      |
| atio |      |
| n/in |      |
| form |      |
| atio |      |
| n.py |      |
| >`__ |      |
| **   |      |
+------+------+------+
| INFO | Prin | DONE |
|      | t    |      |
|      | df   |      |
|      | Info |      |
|      | rmat |      |
|      | ion  |      |
+------+------+------+
| prin | ``jh |
| t    | ta.I |
|      | NFO( |
|      | df,  |
|      | pric |
|      | e='C |
|      | lose |
|      | ')`` |
+------+------+------+
| INFO | Prin | DONE |
| \_TR | t    |      |
| ADES | Trad |      |
|      | es   |      |
|      | Info |      |
|      | rmat |      |
|      | ion  |      |
+------+------+------+
| prin | ``jh |
| t    | ta.I |
|      | NFO_ |
|      | TRAD |
|      | ES(p |
|      | rofi |
|      | t_tr |
|      | ades |
|      | _lis |
|      | t, l |
|      | oss_ |
|      | trad |
|      | es_l |
|      | ist) |
|      | ``   |
+------+------+------+
| **`m |      |
| ath\ |      |
| _fun |      |
| ctio |      |
| ns < |      |
| http |      |
| s:// |      |
| gith |      |
| ub.c |      |
| om/j |      |
| oost |      |
| hoek |      |
| s/jh |      |
| TAli |      |
| b/bl |      |
| ob/m |      |
| aste |      |
| r/jh |      |
| tali |      |
| b/ma |      |
| th_f |      |
| unct |      |
| ions |      |
| /mat |      |
| h_fu |      |
| ncti |      |
| ons. |      |
| py>` |      |
| __** |      |
+------+------+------+
| EXP  | Expo | DONE |
|      | nent |      |
|      | ial  |      |
+------+------+------+
| list | ``jh |
|      | ta.E |
|      | XP(d |
|      | f, p |
|      | rice |
|      | ='Cl |
|      | ose' |
|      | )``  |
+------+------+------+
| LOG  | Loga | DONE |
|      | rith |      |
|      | m    |      |
+------+------+------+
| list | ``jh |
|      | ta.L |
|      | OG(d |
|      | f, p |
|      | rice |
|      | ='Cl |
|      | ose' |
|      | )``  |
+------+------+------+
| LOG1 | Base | DONE |
| 0    | -10  |      |
|      | Loga |      |
|      | rith |      |
|      | m    |      |
+------+------+------+
| list | ``jh |
|      | ta.L |
|      | OG10 |
|      | (df, |
|      |  pri |
|      | ce=' |
|      | Clos |
|      | e')` |
|      | `    |
+------+------+------+
| SQRT | Squa | DONE |
|      | re   |      |
|      | Root |      |
+------+------+------+
| list | ``jh |
|      | ta.S |
|      | QRT( |
|      | df,  |
|      | pric |
|      | e='C |
|      | lose |
|      | ')`` |
+------+------+------+
| ACOS | Arc  | DONE |
|      | Cosi |      |
|      | ne   |      |
+------+------+------+
| list | ``jh |
|      | ta.A |
|      | COS( |
|      | df,  |
|      | pric |
|      | e='C |
|      | lose |
|      | ')`` |
+------+------+------+
| ASIN | Arc  | DONE |
|      | Sine |      |
+------+------+------+
| list | ``jh |
|      | ta.A |
|      | SIN( |
|      | df,  |
|      | pric |
|      | e='C |
|      | lose |
|      | ')`` |
+------+------+------+
| ATAN | Arc  | DONE |
|      | Tang |      |
|      | ent  |      |
+------+------+------+
| list | ``jh |
|      | ta.A |
|      | TAN( |
|      | df,  |
|      | pric |
|      | e='C |
|      | lose |
|      | ')`` |
+------+------+------+
| COS  | Cosi | DONE |
|      | ne   |      |
+------+------+------+
| list | ``jh |
|      | ta.C |
|      | OS(d |
|      | f, p |
|      | rice |
|      | ='Cl |
|      | ose' |
|      | )``  |
+------+------+------+
| SIN  | Sine | DONE |
+------+------+------+
| list | ``jh |
|      | ta.S |
|      | IN(d |
|      | f, p |
|      | rice |
|      | ='Cl |
|      | ose' |
|      | )``  |
+------+------+------+
| TAN  | Tang | DONE |
|      | ent  |      |
+------+------+------+
| list | ``jh |
|      | ta.T |
|      | AN(d |
|      | f, p |
|      | rice |
|      | ='Cl |
|      | ose' |
|      | )``  |
+------+------+------+
| ACOS | Inve | DONE |
| H    | rse  |      |
|      | Hype |      |
|      | rbol |      |
|      | ic   |      |
|      | Cosi |      |
|      | ne   |      |
+------+------+------+
| list | ``jh |
|      | ta.A |
|      | COSH |
|      | (df, |
|      |  pri |
|      | ce=' |
|      | Clos |
|      | e')` |
|      | `    |
+------+------+------+
| ASIN | Inve | DONE |
| H    | rse  |      |
|      | Hype |      |
|      | rbol |      |
|      | ic   |      |
|      | Sine |      |
+------+------+------+
| list | ``jh |
|      | ta.A |
|      | SINH |
|      | (df, |
|      |  pri |
|      | ce=' |
|      | Clos |
|      | e')` |
|      | `    |
+------+------+------+
| ATAN | Inve | DONE |
| H    | rse  |      |
|      | Hype |      |
|      | rbol |      |
|      | ic   |      |
|      | Tang |      |
|      | ent  |      |
+------+------+------+
| list | ``jh |
|      | ta.A |
|      | TANH |
|      | (df, |
|      |  pri |
|      | ce=' |
|      | Clos |
|      | e')` |
|      | `    |
+------+------+------+
| COSH | Hype | DONE |
|      | rbol |      |
|      | ic   |      |
|      | Cosi |      |
|      | ne   |      |
+------+------+------+
| list | ``jh |
|      | ta.C |
|      | OSH( |
|      | df,  |
|      | pric |
|      | e='C |
|      | lose |
|      | ')`` |
+------+------+------+
| SINH | Hype | DONE |
|      | rbol |      |
|      | ic   |      |
|      | Sine |      |
+------+------+------+
| list | ``jh |
|      | ta.S |
|      | INH( |
|      | df,  |
|      | pric |
|      | e='C |
|      | lose |
|      | ')`` |
+------+------+------+
| TANH | Hype | DONE |
|      | rbol |      |
|      | ic   |      |
|      | Tang |      |
|      | ent  |      |
+------+------+------+
| list | ``jh |
|      | ta.T |
|      | ANH( |
|      | df,  |
|      | pric |
|      | e='C |
|      | lose |
|      | ')`` |
+------+------+------+
| PI   | Math | DONE |
|      | emat |      |
|      | ical |      |
|      | cons |      |
|      | tant |      |
|      | PI   |      |
+------+------+------+
| floa | ``jh |
| t    | ta.P |
|      | I()` |
|      | `    |
+------+------+------+
| E    | Math | DONE |
|      | emat |      |
|      | ical |      |
|      | cons |      |
|      | tant |      |
|      | E    |      |
+------+------+------+
| floa | ``jh |
| t    | ta.E |
|      | ()`` |
+------+------+------+
| TAU  | Math | DONE |
|      | emat |      |
|      | ical |      |
|      | cons |      |
|      | tant |      |
|      | TAU  |      |
+------+------+------+
| floa | ``jh |
| t    | ta.T |
|      | AU() |
|      | ``   |
+------+------+------+
| PHI  | Math | DONE |
|      | emat |      |
|      | ical |      |
|      | cons |      |
|      | tant |      |
|      | PHI  |      |
+------+------+------+
| floa | ``jh |
| t    | ta.P |
|      | HI() |
|      | ``   |
+------+------+------+
| CEIL | Ceil | DONE |
|      | ing  |      |
+------+------+------+
| list | ``jh |
|      | ta.C |
|      | EIL( |
|      | df,  |
|      | pric |
|      | e='C |
|      | lose |
|      | ')`` |
+------+------+------+
| FLOO | Floo | DONE |
| R    | r    |      |
+------+------+------+
| list | ``jh |
|      | ta.F |
|      | LOOR |
|      | (df, |
|      |  pri |
|      | ce=' |
|      | Clos |
|      | e')` |
|      | `    |
+------+------+------+
| DEGR | Radi | DONE |
| EES  | ans  |      |
|      | to   |      |
|      | Degr |      |
|      | ees  |      |
+------+------+------+
| list | ``jh |
|      | ta.D |
|      | EGRE |
|      | ES(d |
|      | f, p |
|      | rice |
|      | ='Cl |
|      | ose' |
|      | )``  |
+------+------+------+
| RADI | Degr | DONE |
| ANS  | ees  |      |
|      | to   |      |
|      | Radi |      |
|      | ans  |      |
+------+------+------+
| list | ``jh |
|      | ta.R |
|      | ADIA |
|      | NS(d |
|      | f, p |
|      | rice |
|      | ='Cl |
|      | ose' |
|      | )``  |
+------+------+------+
| ADD  | Addi | DONE |
|      | tion |      |
|      | High |      |
|      | +    |      |
|      | Low  |      |
+------+------+------+
| list | ``jh |
|      | ta.A |
|      | DD(d |
|      | f)`` |
+------+------+------+
| DIV  | Divi | DONE |
|      | sion |      |
|      | High |      |
|      | /    |      |
|      | Low  |      |
+------+------+------+
| list | ``jh |
|      | ta.D |
|      | IV(d |
|      | f)`` |
+------+------+------+
| MAX  | High | DONE |
|      | est  |      |
|      | valu |      |
|      | e    |      |
|      | over |      |
|      | a    |      |
|      | spec |      |
|      | ifie |      |
|      | d    |      |
|      | peri |      |
|      | od   |      |
+------+------+------+
| list | ``jh |
|      | ta.M |
|      | AX(d |
|      | f, n |
|      | , pr |
|      | ice= |
|      | 'Clo |
|      | se') |
|      | ``   |
+------+------+------+
| MAXI | Inde |
| NDEX | x    |
|      | of   |
|      | high |
|      | est  |
|      | valu |
|      | e    |
|      | over |
|      | a    |
|      | spec |
|      | ifie |
|      | d    |
|      | peri |
|      | od   |
+------+------+------+
| MIN  | Lowe | DONE |
|      | st   |      |
|      | valu |      |
|      | e    |      |
|      | over |      |
|      | a    |      |
|      | spec |      |
|      | ifie |      |
|      | d    |      |
|      | peri |      |
|      | od   |      |
+------+------+------+
| list | ``jh |
|      | ta.M |
|      | IN(d |
|      | f, n |
|      | , pr |
|      | ice= |
|      | 'Clo |
|      | se') |
|      | ``   |
+------+------+------+
| MINI | Inde |
| NDEX | x    |
|      | of   |
|      | lowe |
|      | st   |
|      | valu |
|      | e    |
|      | over |
|      | a    |
|      | spec |
|      | ifie |
|      | d    |
|      | peri |
|      | od   |
+------+------+------+
| MINM | Lowe |
| AX   | st   |
|      | and  |
|      | High |
|      | est  |
|      | valu |
|      | es   |
|      | over |
|      | a    |
|      | spec |
|      | ifie |
|      | d    |
|      | peri |
|      | od   |
+------+------+------+
| MINM | Inde |
| AXIN | xes  |
| DEX  | of   |
|      | lowe |
|      | st   |
|      | and  |
|      | high |
|      | est  |
|      | valu |
|      | es   |
|      | over |
|      | a    |
|      | spec |
|      | ifie |
|      | d    |
|      | peri |
|      | od   |
+------+------+------+
| MULT | Mult | DONE |
|      | iply |      |
|      | High |      |
|      | \*   |      |
|      | Low  |      |
+------+------+------+
| list | ``jh |
|      | ta.M |
|      | ULT( |
|      | df)` |
|      | `    |
+------+------+------+
| SUB  | Subt | DONE |
|      | ract |      |
|      | ion  |      |
|      | High |      |
|      | -    |      |
|      | Low  |      |
+------+------+------+
| list | ``jh |
|      | ta.S |
|      | UB(d |
|      | f)`` |
+------+------+------+
| SUM  | Summ | DONE |
|      | atio |      |
|      | n    |      |
+------+------+------+
| list | ``jh |
|      | ta.S |
|      | UM(d |
|      | f, n |
|      | , pr |
|      | ice= |
|      | 'Clo |
|      | se') |
|      | ``   |
+------+------+------+
| **`m |      |
| omen |      |
| tum\ |      |
| _ind |      |
| icat |      |
| ors  |      |
| <htt |      |
| ps:/ |      |
| /git |      |
| hub. |      |
| com/ |      |
| joos |      |
| thoe |      |
| ks/j |      |
| hTAl |      |
| ib/b |      |
| lob/ |      |
| mast |      |
| er/j |      |
| htal |      |
| ib/m |      |
| omen |      |
| tum_ |      |
| indi |      |
| cato |      |
| rs/m |      |
| omen |      |
| tum_ |      |
| indi |      |
| cato |      |
| rs.p |      |
| y>`_ |      |
| _**  |      |
+------+------+------+
| ADX  | Aver |
|      | age  |
|      | Dire |
|      | ctio |
|      | nal  |
|      | Move |
|      | ment |
|      | Inde |
|      | x    |
+------+------+------+
| ADXR | Aver |
|      | age  |
|      | Dire |
|      | ctio |
|      | nal  |
|      | Move |
|      | ment |
|      | Inde |
|      | x    |
|      | Rati |
|      | ng   |
+------+------+------+
| APO  | Abso | DONE |
|      | lute |      |
|      | Pric |      |
|      | e    |      |
|      | Osci |      |
|      | llat |      |
|      | or   |      |
+------+------+------+
| list | ``jh |
|      | ta.A |
|      | PO(d |
|      | f, n |
|      | _fas |
|      | t, n |
|      | _slo |
|      | w, p |
|      | rice |
|      | ='Cl |
|      | ose' |
|      | )``  |
+------+------+------+
| AROO | Aroo |
| N    | n    |
+------+------+------+
| AROO | Aroo |
| NOSC | n    |
|      | Osci |
|      | llat |
|      | or   |
+------+------+------+
| BOP  | Bala |
|      | nce  |
|      | Of   |
|      | Powe |
|      | r    |
+------+------+------+
| CCI  | Comm |
|      | odit |
|      | y    |
|      | Chan |
|      | nel  |
|      | Inde |
|      | x    |
+------+------+------+
| CMO  | Chan |
|      | de   |
|      | Mome |
|      | ntum |
|      | Osci |
|      | llat |
|      | or   |
+------+------+------+
| DX   | Dire |
|      | ctio |
|      | nal  |
|      | Move |
|      | ment |
|      | Inde |
|      | x    |
+------+------+------+
| IMI  | Intr | DONE |
|      | aday |      |
|      | Mome |      |
|      | ntum |      |
|      | Inde |      |
|      | x    |      |
+------+------+------+
| list | ``jh |
|      | ta.I |
|      | MI(d |
|      | f)`` |
+------+------+------+
| MACD | Movi |
|      | ng   |
|      | Aver |
|      | age  |
|      | Conv |
|      | erge |
|      | nce/ |
|      | Dive |
|      | rgen |
|      | ce   |
+------+------+------+
| MACD | MACD |
| EXT  | with |
|      | cont |
|      | roll |
|      | able |
|      | MA   |
|      | type |
+------+------+------+
| MACD | Movi |
| FIX  | ng   |
|      | Aver |
|      | age  |
|      | Conv |
|      | erge |
|      | nce/ |
|      | Dive |
|      | rgen |
|      | ce   |
|      | Fix  |
|      | 12/2 |
|      | 6    |
+------+------+------+
| MFI  | Mone |
|      | y    |
|      | Flow |
|      | Inde |
|      | x    |
+------+------+------+
| MINU | Minu |
| S\_D | s    |
| I    | Dire |
|      | ctio |
|      | nal  |
|      | Indi |
|      | cato |
|      | r    |
+------+------+------+
| MINU | Minu |
| S\_D | s    |
| M    | Dire |
|      | ctio |
|      | nal  |
|      | Move |
|      | ment |
+------+------+------+
| MOM  | Mome | DONE |
|      | ntum |      |
+------+------+------+
| list | ``jh |
|      | ta.M |
|      | OM(d |
|      | f, n |
|      | , pr |
|      | ice= |
|      | 'Clo |
|      | se') |
|      | ``   |
+------+------+------+
| PLUS | Plus |
| \_DI | Dire |
|      | ctio |
|      | nal  |
|      | Indi |
|      | cato |
|      | r    |
+------+------+------+
| PLUS | Plus |
| \_DM | Dire |
|      | ctio |
|      | nal  |
|      | Move |
|      | ment |
+------+------+------+
| PPO  | Perc |
|      | enta |
|      | ge   |
|      | Pric |
|      | e    |
|      | Osci |
|      | llat |
|      | or   |
+------+------+------+
| ROC  | Rate | DONE |
|      | of   |      |
|      | Chan |      |
|      | ge   |      |
+------+------+------+
| list | ``jh |
|      | ta.R |
|      | OC(d |
|      | f, n |
|      | , pr |
|      | ice= |
|      | 'Clo |
|      | se') |
|      | ``   |
+------+------+------+
| ROCP | Rate | DONE |
|      | of   |      |
|      | Chan |      |
|      | ge   |      |
|      | Perc |      |
|      | enta |      |
|      | ge   |      |
+------+------+------+
| list | ``jh |
|      | ta.R |
|      | OCP( |
|      | df,  |
|      | n, p |
|      | rice |
|      | ='Cl |
|      | ose' |
|      | )``  |
+------+------+------+
| ROCR | Rate | DONE |
|      | of   |      |
|      | Chan |      |
|      | ge   |      |
|      | Rati |      |
|      | o    |      |
+------+------+------+
| list | ``jh |
|      | ta.R |
|      | OCR( |
|      | df,  |
|      | n, p |
|      | rice |
|      | ='Cl |
|      | ose' |
|      | )``  |
+------+------+------+
| ROCR | Rate | DONE |
| 100  | of   |      |
|      | Chan |      |
|      | ge   |      |
|      | Rati |      |
|      | o    |      |
|      | 100  |      |
|      | scal |      |
|      | e    |      |
+------+------+------+
| list | ``jh |
|      | ta.R |
|      | OCR1 |
|      | 00(d |
|      | f, n |
|      | , pr |
|      | ice= |
|      | 'Clo |
|      | se') |
|      | ``   |
+------+------+------+
| RSI  | Rela | DONE |
|      | tive |      |
|      | Stre |      |
|      | ngth |      |
|      | Inde |      |
|      | x    |      |
+------+------+------+
| list | ``jh |
|      | ta.R |
|      | SI(d |
|      | f, n |
|      | , pr |
|      | ice= |
|      | 'Clo |
|      | se') |
|      | ``   |
+------+------+------+
| STOC | Stoc |
| H    | hast |
|      | ic   |
+------+------+------+
| STOC | Stoc |
| HF   | hast |
|      | ic   |
|      | Fast |
+------+------+------+
| STOC | Stoc |
| HRSI | hast |
|      | ic   |
|      | Rela |
|      | tive |
|      | Stre |
|      | ngth |
|      | Inde |
|      | x    |
+------+------+------+
| TRIX | 1-da |
|      | y    |
|      | Rate |
|      | -Of- |
|      | Chan |
|      | ge   |
|      | (ROC |
|      | )    |
|      | of a |
|      | Trip |
|      | le   |
|      | Smoo |
|      | th   |
|      | EMA  |
+------+------+------+
| ULTO | Ulti |
| SC   | mate |
|      | Osci |
|      | llat |
|      | or   |
+------+------+------+
| WILL | Will | DONE |
| R    | iams |      |
|      | '    |      |
|      | %R   |      |
+------+------+------+
| list | ``jh |
|      | ta.W |
|      | ILLR |
|      | (df, |
|      |  n)` |
|      | `    |
+------+------+------+
| **`o |      |
| verl |      |
| ap\_ |      |
| stud |      |
| ies  |      |
| <htt |      |
| ps:/ |      |
| /git |      |
| hub. |      |
| com/ |      |
| joos |      |
| thoe |      |
| ks/j |      |
| hTAl |      |
| ib/b |      |
| lob/ |      |
| mast |      |
| er/j |      |
| htal |      |
| ib/o |      |
| verl |      |
| ap_s |      |
| tudi |      |
| es/o |      |
| verl |      |
| ap_s |      |
| tudi |      |
| es.p |      |
| y>`_ |      |
| _**  |      |
+------+------+------+
| BBAN | Boll | DONE |
| DS   | inge |      |
|      | r    |      |
|      | Band |      |
|      | s    |      |
+------+------+------+
| dict | ``jh |
| of   | ta.B |
| list | BAND |
| s    | S(df |
|      | , n, |
|      |  f=2 |
|      | )``  |
+------+------+------+
| BBAN | Boll | DONE |
| DW   | inge |      |
|      | r    |      |
|      | Band |      |
|      | Widt |      |
|      | h    |      |
+------+------+------+
| list | ``jh |
|      | ta.B |
|      | BAND |
|      | W(df |
|      | , n, |
|      |  f=2 |
|      | )``  |
+------+------+------+
| DEMA | Doub |
|      | le   |
|      | Expo |
|      | nent |
|      | ial  |
|      | Movi |
|      | ng   |
|      | Aver |
|      | age  |
+------+------+------+
| EMA  | Expo |
|      | nent |
|      | ial  |
|      | Movi |
|      | ng   |
|      | Aver |
|      | age  |
+------+------+------+
| ENVP | Enve | DONE |
|      | lope |      |
|      | Perc |      |
|      | ent  |      |
+------+------+------+
| dict | ``jh |
| of   | ta.E |
| list | NVP( |
| s    | df,  |
|      | pct= |
|      | .01, |
|      |  pri |
|      | ce=' |
|      | Clos |
|      | e')` |
|      | `    |
+------+------+------+
| KAMA | Kauf |
|      | man  |
|      | Adap |
|      | tive |
|      | Movi |
|      | ng   |
|      | Aver |
|      | age  |
+------+------+------+
| MA   | Movi |
|      | ng   |
|      | Aver |
|      | age  |
+------+------+------+
| MAMA | MESA |
|      | Adap |
|      | tive |
|      | Movi |
|      | ng   |
|      | Aver |
|      | age  |
+------+------+------+
| MAVP | Movi |
|      | ng   |
|      | Aver |
|      | age  |
|      | with |
|      | Vari |
|      | able |
|      | Peri |
|      | od   |
+------+------+------+
| MIDP | MidP | DONE |
| OINT | oint |      |
|      | over |      |
|      | peri |      |
|      | od   |      |
+------+------+------+
| list | ``jh |
|      | ta.M |
|      | IDPO |
|      | INT( |
|      | df,  |
|      | n, p |
|      | rice |
|      | ='Cl |
|      | ose' |
|      | )``  |
+------+------+------+
| MIDP | MidP | DONE |
| RICE | oint |      |
|      | Pric |      |
|      | e    |      |
|      | over |      |
|      | peri |      |
|      | od   |      |
+------+------+------+
| list | ``jh |
|      | ta.M |
|      | IDPR |
|      | ICE( |
|      | df,  |
|      | n)`` |
+------+------+------+
| MMR  | Maye | DONE |
|      | r    |      |
|      | Mult |      |
|      | iple |      |
|      | Rati |      |
|      | o    |      |
+------+------+------+
| list | ``jh |
|      | ta.M |
|      | MR(d |
|      | f, n |
|      | =200 |
|      | , pr |
|      | ice= |
|      | 'Clo |
|      | se') |
|      | ``   |
+------+------+------+
| SAR  | Para | DONE |
|      | boli |      |
|      | c    |      |
|      | SAR  |      |
+------+------+------+
| list | ``jh |
|      | ta.S |
|      | AR(d |
|      | f, a |
|      | f_st |
|      | ep=. |
|      | 02,  |
|      | af_m |
|      | ax=. |
|      | 2)`` |
+------+------+------+
| SARE | Para |
| XT   | boli |
|      | c    |
|      | SAR  |
|      | -    |
|      | Exte |
|      | nded |
+------+------+------+
| SMA  | Simp | DONE |
|      | le   |      |
|      | Movi |      |
|      | ng   |      |
|      | Aver |      |
|      | age  |      |
+------+------+------+
| list | ``jh |
|      | ta.S |
|      | MA(d |
|      | f, n |
|      | , pr |
|      | ice= |
|      | 'Clo |
|      | se') |
|      | ``   |
+------+------+------+
| T3   | Trip |
|      | le   |
|      | Expo |
|      | nent |
|      | ial  |
|      | Movi |
|      | ng   |
|      | Aver |
|      | age  |
|      | (T3) |
+------+------+------+
| TEMA | Trip |
|      | le   |
|      | Expo |
|      | nent |
|      | ial  |
|      | Movi |
|      | ng   |
|      | Aver |
|      | age  |
+------+------+------+
| TRIM | Tria | DONE |
| A    | ngul |      |
|      | ar   |      |
|      | Movi |      |
|      | ng   |      |
|      | Aver |      |
|      | age  |      |
+------+------+------+
| list | ``jh |
|      | ta.T |
|      | RIMA |
|      | (df, |
|      |  n,  |
|      | pric |
|      | e='C |
|      | lose |
|      | ')`` |
+------+------+------+
| WMA  | Weig |
|      | hted |
|      | Movi |
|      | ng   |
|      | Aver |
|      | age  |
+------+------+------+
| **`p |      |
| atte |      |
| rn\_ |      |
| reco |      |
| gnit |      |
| ion  |      |
| <htt |      |
| ps:/ |      |
| /git |      |
| hub. |      |
| com/ |      |
| joos |      |
| thoe |      |
| ks/j |      |
| hTAl |      |
| ib/b |      |
| lob/ |      |
| mast |      |
| er/j |      |
| htal |      |
| ib/p |      |
| atte |      |
| rn_r |      |
| ecog |      |
| niti |      |
| on/p |      |
| atte |      |
| rn_r |      |
| ecog |      |
| niti |      |
| on.p |      |
| y>`_ |      |
| _**  |      |
+------+------+------+
| CDL2 | Two  |
| CROW | Crow |
| S    | s    |
+------+------+------+
| CDL3 | Thre |
| BLAC | e    |
| KCRO | Blac |
| WS   | k    |
|      | Crow |
|      | s    |
+------+------+------+
| CDL3 | Thre |
| INSI | e    |
| DE   | Insi |
|      | de   |
|      | Up/D |
|      | own  |
+------+------+------+
| CDL3 | Thre |
| LINE | e-Li |
| STRI | ne   |
| KE   | Stri |
|      | ke   |
+------+------+------+
| CDL3 | Thre |
| OUTS | e    |
| IDE  | Outs |
|      | ide  |
|      | Up/D |
|      | own  |
+------+------+------+
| CDL3 | Thre |
| STAR | e    |
| SINS | Star |
| OUTH | s    |
|      | In   |
|      | The  |
|      | Sout |
|      | h    |
+------+------+------+
| CDL3 | Thre |
| WHIT | e    |
| ESOL | Adva |
| DIER | ncin |
| S    | g    |
|      | Whit |
|      | e    |
|      | Sold |
|      | iers |
+------+------+------+
| CDLA | Aban |
| BAND | done |
| ONED | d    |
| BABY | Baby |
+------+------+------+
| CDLA | Adva |
| DVAN | nce  |
| CEBL | Bloc |
| OCK  | k    |
+------+------+------+
| CDLB | Belt |
| ELTH | -hol |
| OLD  | d    |
+------+------+------+
| CDLB | Brea |
| REAK | kawa |
| AWAY | y    |
+------+------+------+
| CDLC | Clos |
| LOSI | ing  |
| NGMA | Maru |
| RUBO | bozu |
| ZU   |      |
+------+------+------+
| CDLC | Conc |
| ONSE | eali |
| ALBA | ng   |
| BYSW | Baby |
| ALL  | Swal |
|      | low  |
+------+------+------+
| CDLC | Coun |
| OUNT | tera |
| ERAT | ttac |
| TACK | k    |
+------+------+------+
| CDLD | Dark |
| ARKC | Clou |
| LOUD | d    |
| COVE | Cove |
| R    | r    |
+------+------+------+
| CDLD | Doji |
| OJI  |      |
+------+------+------+
| CDLD | Doji |
| OJIS | Star |
| TAR  |      |
+------+------+------+
| CDLD | Drag |
| RAGO | onfl |
| NFLY | y    |
| DOJI | Doji |
+------+------+------+
| CDLE | Engu |
| NGUL | lfin |
| FING | g    |
|      | Patt |
|      | ern  |
+------+------+------+
| CDLE | Even |
| VENI | ing  |
| NGDO | Doji |
| JIST | Star |
| AR   |      |
+------+------+------+
| CDLE | Even |
| VENI | ing  |
| NGST | Star |
| AR   |      |
+------+------+------+
| CDLG | Up/D |
| APSI | own- |
| DESI | gap  |
| DEWH | side |
| ITE  | -by- |
|      | side |
|      | whit |
|      | e    |
|      | line |
|      | s    |
+------+------+------+
| CDLG | Grav |
| RAVE | esto |
| STON | ne   |
| EDOJ | Doji |
| I    |      |
+------+------+------+
| CDLH | Hamm |
| AMME | er   |
| R    |      |
+------+------+------+
| CDLH | Hang |
| ANGI | ing  |
| NGMA | Man  |
| N    |      |
+------+------+------+
| CDLH | Hara |
| ARAM | mi   |
| I    | Patt |
|      | ern  |
+------+------+------+
| CDLH | Hara |
| ARAM | mi   |
| ICRO | Cros |
| SS   | s    |
|      | Patt |
|      | ern  |
+------+------+------+
| CDLH | High |
| IGHW | -Wav |
| AVE  | e    |
|      | Cand |
|      | le   |
+------+------+------+
| CDLH | Hikk |
| IKKA | ake  |
| KE   | Patt |
|      | ern  |
+------+------+------+
| CDLH | Modi |
| IKKA | fied |
| KEMO | Hikk |
| D    | ake  |
|      | Patt |
|      | ern  |
+------+------+------+
| CDLH | Homi |
| OMIN | ng   |
| GPIG | Pige |
| EON  | on   |
+------+------+------+
| CDLI | Iden |
| DENT | tica |
| ICAL | l    |
| 3CRO | Thre |
| WS   | e    |
|      | Crow |
|      | s    |
+------+------+------+
| CDLI | In-N |
| NNEC | eck  |
| K    | Patt |
|      | ern  |
+------+------+------+
| CDLI | Inve |
| NVER | rted |
| TEDH | Hamm |
| AMME | er   |
| R    |      |
+------+------+------+
| CDLK | Kick |
| ICKI | ing  |
| NG   |      |
+------+------+------+
| CDLK | Kick |
| ICKI | ing  |
| NGBY | -    |
| LENG | bull |
| TH   | /bea |
|      | r    |
|      | dete |
|      | rmin |
|      | ed   |
|      | by   |
|      | the  |
|      | long |
|      | er   |
|      | maru |
|      | bozu |
+------+------+------+
| CDLL | Ladd |
| ADDE | er   |
| RBOT | Bott |
| TOM  | om   |
+------+------+------+
| CDLL | Long |
| ONGL | Legg |
| EGGE | ed   |
| DDOJ | Doji |
| I    |      |
+------+------+------+
| CDLL | Long |
| ONGL | Line |
| INE  | Cand |
|      | le   |
+------+------+------+
| CDLM | Maru |
| ARUB | bozu |
| OZU  |      |
+------+------+------+
| CDLM | Matc |
| ATCH | hing |
| INGL | Low  |
| OW   |      |
+------+------+------+
| CDLM | Mat  |
| ATHO | Hold |
| LD   |      |
+------+------+------+
| CDLM | Morn |
| ORNI | ing  |
| NGDO | Doji |
| JIST | Star |
| AR   |      |
+------+------+------+
| CDLM | Morn |
| ORNI | ing  |
| NGST | Star |
| AR   |      |
+------+------+------+
| CDLO | On-N |
| NNEC | eck  |
| K    | Patt |
|      | ern  |
+------+------+------+
| CDLP | Pier |
| IERC | cing |
| ING  | Patt |
|      | ern  |
+------+------+------+
| CDLR | Rick |
| ICKS | shaw |
| HAWM | Man  |
| AN   |      |
+------+------+------+
| CDLR | Risi |
| ISEF | ng/F |
| ALL3 | alli |
| METH | ng   |
| ODS  | Thre |
|      | e    |
|      | Meth |
|      | ods  |
+------+------+------+
| CDLS | Sepa |
| EPAR | rati |
| ATIN | ng   |
| GLIN | Line |
| ES   | s    |
+------+------+------+
| CDLS | Shoo |
| HOOT | ting |
| INGS | Star |
| TAR  |      |
+------+------+------+
| CDLS | Shor |
| HORT | t    |
| LINE | Line |
|      | Cand |
|      | le   |
+------+------+------+
| CDLS | Spin |
| PINN | ning |
| INGT | Top  |
| OP   |      |
+------+------+------+
| CDLS | Stal |
| TALL | led  |
| EDPA | Patt |
| TTER | ern  |
| N    |      |
+------+------+------+
| CDLS | Stic |
| TICK | k    |
| SAND | Sand |
| WICH | wich |
+------+------+------+
| CDLT | Taku |
| AKUR | ri   |
| I    | (Dra |
|      | gonf |
|      | ly   |
|      | Doji |
|      | with |
|      | very |
|      | long |
|      | lowe |
|      | r    |
|      | shad |
|      | ow)  |
+------+------+------+
| CDLT | Tasu |
| ASUK | ki   |
| IGAP | Gap  |
+------+------+------+
| CDLT | Thru |
| HRUS | stin |
| TING | g    |
|      | Patt |
|      | ern  |
+------+------+------+
| CDLT | Tris |
| RIST | tar  |
| AR   | Patt |
|      | ern  |
+------+------+------+
| CDLU | Uniq |
| NIQU | ue   |
| E3RI | 3    |
| VER  | Rive |
|      | r    |
+------+------+------+
| CDLU | Upsi |
| PSID | de   |
| EGAP | Gap  |
| 2CRO | Two  |
| WS   | Crow |
|      | s    |
+------+------+------+
| CDLX | Upsi |
| SIDE | de/D |
| GAP3 | owns |
| METH | ide  |
| ODS  | Gap  |
|      | Thre |
|      | e    |
|      | Meth |
|      | ods  |
+------+------+------+
| **`p |      |
| rice |      |
| \_tr |      |
| ansf |      |
| orm  |      |
| <htt |      |
| ps:/ |      |
| /git |      |
| hub. |      |
| com/ |      |
| joos |      |
| thoe |      |
| ks/j |      |
| hTAl |      |
| ib/b |      |
| lob/ |      |
| mast |      |
| er/j |      |
| htal |      |
| ib/p |      |
| rice |      |
| _tra |      |
| nsfo |      |
| rm/p |      |
| rice |      |
| _tra |      |
| nsfo |      |
| rm.p |      |
| y>`_ |      |
| _**  |      |
+------+------+------+
| AVGP | Aver | DONE |
| RICE | age  |      |
|      | Pric |      |
|      | e    |      |
+------+------+------+
| list | ``jh |
|      | ta.A |
|      | VGPR |
|      | ICE( |
|      | df)` |
|      | `    |
+------+------+------+
| MEDP | Medi | DONE |
| RICE | an   |      |
|      | Pric |      |
|      | e    |      |
+------+------+------+
| list | ``jh |
|      | ta.M |
|      | EDPR |
|      | ICE( |
|      | df)` |
|      | `    |
+------+------+------+
| TYPP | Typi | DONE |
| RICE | cal  |      |
|      | Pric |      |
|      | e    |      |
+------+------+------+
| list | ``jh |
|      | ta.T |
|      | YPPR |
|      | ICE( |
|      | df)` |
|      | `    |
+------+------+------+
| WCLP | Weig | DONE |
| RICE | hted |      |
|      | Clos |      |
|      | e    |      |
|      | Pric |      |
|      | e    |      |
+------+------+------+
| list | ``jh |
|      | ta.W |
|      | CLPR |
|      | ICE( |
|      | df)` |
|      | `    |
+------+------+------+
| **`s |      |
| tati |      |
| stic |      |
| \_fu |      |
| ncti |      |
| ons  |      |
| <htt |      |
| ps:/ |      |
| /git |      |
| hub. |      |
| com/ |      |
| joos |      |
| thoe |      |
| ks/j |      |
| hTAl |      |
| ib/b |      |
| lob/ |      |
| mast |      |
| er/j |      |
| htal |      |
| ib/s |      |
| tati |      |
| stic |      |
| _fun |      |
| ctio |      |
| ns/s |      |
| tati |      |
| stic |      |
| _fun |      |
| ctio |      |
| ns.p |      |
| y>`_ |      |
| _**  |      |
+------+------+------+
| MEAN | Arit | DONE |
|      | hmet |      |
|      | ic   |      |
|      | mean |      |
|      | (ave |      |
|      | rage |      |
|      | )    |      |
|      | of   |      |
|      | data |      |
+------+------+------+
| list | ``jh |
|      | ta.M |
|      | EAN( |
|      | df,  |
|      | n, p |
|      | rice |
|      | ='Cl |
|      | ose' |
|      | )``  |
+------+------+------+
| HARM | Harm | DONE |
| ONIC | onic |      |
| \_ME | mean |      |
| AN   | of   |      |
|      | data |      |
+------+------+------+
| list | ``jh |
|      | ta.H |
|      | ARMO |
|      | NIC_ |
|      | MEAN |
|      | (df, |
|      |  n,  |
|      | pric |
|      | e='C |
|      | lose |
|      | ')`` |
+------+------+------+
| MEDI | Medi | DONE |
| AN   | an   |      |
|      | (mid |      |
|      | dle  |      |
|      | valu |      |
|      | e)   |      |
|      | of   |      |
|      | data |      |
+------+------+------+
| list | ``jh |
|      | ta.M |
|      | EDIA |
|      | N(df |
|      | , n, |
|      |  pri |
|      | ce=' |
|      | Clos |
|      | e')` |
|      | `    |
+------+------+------+
| MEDI | Low  | DONE |
| AN\_ | medi |      |
| LOW  | an   |      |
|      | of   |      |
|      | data |      |
+------+------+------+
| list | ``jh |
|      | ta.M |
|      | EDIA |
|      | N_LO |
|      | W(df |
|      | , n, |
|      |  pri |
|      | ce=' |
|      | Clos |
|      | e')` |
|      | `    |
+------+------+------+
| MEDI | High | DONE |
| AN\_ | medi |      |
| HIGH | an   |      |
|      | of   |      |
|      | data |      |
+------+------+------+
| list | ``jh |
|      | ta.M |
|      | EDIA |
|      | N_HI |
|      | GH(d |
|      | f, n |
|      | , pr |
|      | ice= |
|      | 'Clo |
|      | se') |
|      | ``   |
+------+------+------+
| MEDI | Medi | DONE |
| AN\_ | an,  |      |
| GROU | or   |      |
| PED  | 50th |      |
|      | perc |      |
|      | enti |      |
|      | le,  |      |
|      | of   |      |
|      | grou |      |
|      | ped  |      |
|      | data |      |
+------+------+------+
| list | ``jh |
|      | ta.M |
|      | EDIA |
|      | N_GR |
|      | OUPE |
|      | D(df |
|      | , n, |
|      |  pri |
|      | ce=' |
|      | Clos |
|      | e',  |
|      | inte |
|      | rval |
|      | =1)` |
|      | `    |
+------+------+------+
| MODE | Mode | DONE |
|      | (mos |      |
|      | t    |      |
|      | comm |      |
|      | on   |      |
|      | valu |      |
|      | e)   |      |
|      | of   |      |
|      | disc |      |
|      | rete |      |
|      | data |      |
+------+------+------+
| list | ``jh |
|      | ta.M |
|      | ODE( |
|      | df,  |
|      | n, p |
|      | rice |
|      | ='Cl |
|      | ose' |
|      | )``  |
+------+------+------+
| PSTD | Popu | DONE |
| EV   | lati |      |
|      | on   |      |
|      | stan |      |
|      | dard |      |
|      | devi |      |
|      | atio |      |
|      | n    |      |
|      | of   |      |
|      | data |      |
+------+------+------+
| list | ``jh |
|      | ta.P |
|      | STDE |
|      | V(df |
|      | , n, |
|      |  pri |
|      | ce=' |
|      | Clos |
|      | e',  |
|      | mu=N |
|      | one) |
|      | ``   |
+------+------+------+
| PVAR | Popu | DONE |
| IANC | lati |      |
| E    | on   |      |
|      | vari |      |
|      | ance |      |
|      | of   |      |
|      | data |      |
+------+------+------+
| list | ``jh |
|      | ta.P |
|      | VARI |
|      | ANCE |
|      | (df, |
|      |  n,  |
|      | pric |
|      | e='C |
|      | lose |
|      | ', m |
|      | u=No |
|      | ne)` |
|      | `    |
+------+------+------+
| STDE | Samp | DONE |
| V    | le   |      |
|      | stan |      |
|      | dard |      |
|      | devi |      |
|      | atio |      |
|      | n    |      |
|      | of   |      |
|      | data |      |
+------+------+------+
| list | ``jh |
|      | ta.S |
|      | TDEV |
|      | (df, |
|      |  n,  |
|      | pric |
|      | e='C |
|      | lose |
|      | ', x |
|      | bar= |
|      | None |
|      | )``  |
+------+------+------+
| VARI | Samp | DONE |
| ANCE | le   |      |
|      | vari |      |
|      | ance |      |
|      | of   |      |
|      | data |      |
+------+------+------+
| list | ``jh |
|      | ta.V |
|      | ARIA |
|      | NCE( |
|      | df,  |
|      | n, p |
|      | rice |
|      | ='Cl |
|      | ose' |
|      | , xb |
|      | ar=N |
|      | one) |
|      | ``   |
+------+------+------+
| COV  | Cova | DONE |
|      | rian |      |
|      | ce   |      |
+------+------+------+
| floa | ``jh |
| t    | ta.C |
|      | OV(l |
|      | ist1 |
|      | , li |
|      | st2) |
|      | ``   |
+------+------+------+
| COVA | Cova | DONE |
| RIAN | rian |      |
| CE   | ce   |      |
+------+------+------+
| list | ``jh |
|      | ta.C |
|      | OVAR |
|      | IANC |
|      | E(df |
|      | 1, d |
|      | f2,  |
|      | n, p |
|      | rice |
|      | 1='C |
|      | lose |
|      | ', p |
|      | rice |
|      | 2='C |
|      | lose |
|      | ')`` |
+------+------+------+
| BETA | Beta | DONE |
+------+------+------+
| list | ``jh |
|      | ta.B |
|      | ETA( |
|      | df1, |
|      |  df2 |
|      | , n, |
|      |  pri |
|      | ce1= |
|      | 'Clo |
|      | se', |
|      |  pri |
|      | ce2= |
|      | 'Clo |
|      | se') |
|      | ``   |
+------+------+------+
| LSR  | Leas | DONE |
|      | t    |      |
|      | Squa |      |
|      | res  |      |
|      | Regr |      |
|      | essi |      |
|      | on   |      |
+------+------+------+
| list | ``jh |
|      | ta.L |
|      | SR(d |
|      | f, p |
|      | rice |
|      | ='Cl |
|      | ose' |
|      | , pr |
|      | edic |
|      | tion |
|      | s_in |
|      | t=0) |
|      | ``   |
+------+------+------+
| SLR  | Simp | DONE |
|      | le   |      |
|      | Line |      |
|      | ar   |      |
|      | Regr |      |
|      | essi |      |
|      | on   |      |
+------+------+------+
| list | ``jh |
|      | ta.S |
|      | LR(d |
|      | f, p |
|      | rice |
|      | ='Cl |
|      | ose' |
|      | , pr |
|      | edic |
|      | tion |
|      | s_in |
|      | t=0) |
|      | ``   |
+------+------+------+
| **`v |      |
| olat |      |
| ilit |      |
| y\_i |      |
| ndic |      |
| ator |      |
| s <h |      |
| ttps |      |
| ://g |      |
| ithu |      |
| b.co |      |
| m/jo |      |
| osth |      |
| oeks |      |
| /jhT |      |
| Alib |      |
| /blo |      |
| b/ma |      |
| ster |      |
| /jht |      |
| alib |      |
| /vol |      |
| atil |      |
| ity_ |      |
| indi |      |
| cato |      |
| rs/v |      |
| olat |      |
| ilit |      |
| y_in |      |
| dica |      |
| tors |      |
| .py> |      |
| `__* |      |
| *    |      |
+------+------+------+
| ATR  | Aver | DONE |
|      | age  |      |
|      | True |      |
|      | Rang |      |
|      | e    |      |
+------+------+------+
| list | ``jh |
|      | ta.A |
|      | TR(d |
|      | f, n |
|      | )``  |
+------+------+------+
| NATR | Norm |
|      | aliz |
|      | ed   |
|      | Aver |
|      | age  |
|      | True |
|      | Rang |
|      | e    |
+------+------+------+
| TRAN | True | DONE |
| GE   | Rang |      |
|      | e    |      |
+------+------+------+
| list | ``jh |
|      | ta.T |
|      | RANG |
|      | E(df |
|      | )``  |
+------+------+------+
| **`v |      |
| olum |      |
| e\_i |      |
| ndic |      |
| ator |      |
| s <h |      |
| ttps |      |
| ://g |      |
| ithu |      |
| b.co |      |
| m/jo |      |
| osth |      |
| oeks |      |
| /jhT |      |
| Alib |      |
| /blo |      |
| b/ma |      |
| ster |      |
| /jht |      |
| alib |      |
| /vol |      |
| ume_ |      |
| indi |      |
| cato |      |
| rs/v |      |
| olum |      |
| e_in |      |
| dica |      |
| tors |      |
| .py> |      |
| `__* |      |
| *    |      |
+------+------+------+
| AD   | Chai | DONE |
|      | kin  |      |
|      | A/D  |      |
|      | Line |      |
+------+------+------+
| list | ``jh |
|      | ta.A |
|      | D(df |
|      | )``  |
+------+------+------+
| ADOS | Chai |
| C    | kin  |
|      | A/D  |
|      | Osci |
|      | llat |
|      | or   |
+------+------+------+
| OBV  | On   | DONE |
|      | Bala |      |
|      | nce  |      |
|      | Volu |      |
|      | me   |      |
+------+------+------+
| list | ``jh |
|      | ta.O |
|      | BV(d |
|      | f)`` |
+------+------+------+

.. |Open In Colab| image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/example/example-1-plot.ipynb
.. |Open In Colab| image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/example/example-2-plot.ipynb
.. |Open In Colab| image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/example/example-3-plot.ipynb
.. |Open In Colab| image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/example/example-4-plot-quandl.ipynb
.. |Open In Colab| image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/example/example-5-plot-quandl.ipynb
.. |Open In Colab| image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/example/example-6-plot-quandl.ipynb
.. |Open In Colab| image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/example/example-7-quandl-2-df.ipynb
.. |Open In Colab| image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/example/example-8-alphavantage-2-df.ipynb
.. |Open In Colab| image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/example/example-9-cryptocompare-2-df.ipynb
.. |Open In Colab| image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/example/example-10-df-numpy-pandas.ipynb
