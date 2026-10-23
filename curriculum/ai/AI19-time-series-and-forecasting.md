# AI19 — Time Series & Forecasting

**Track:** AI & ML · **Prerequisite:** AI3, F4 · **Elective** · **Time:** 4 weeks, 60 hours · **Project:** elective

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../progress.md)

## Purpose

Build forecasts that respect time: temporal splits, autocorrelation, seasonality, trend, uncertainty, and backtesting. You will compare simple baselines against statistical and ML models and report forecast error honestly.

## Outcomes

You can:

- explore a time series for trend, seasonality, and structural breaks;
- build naive, seasonal-naive, and drift baselines;
- use exponential smoothing and ARIMA;
- build lag/rolling features without leakage;
- backtest with rolling or expanding windows;
- evaluate with MAE, RMSE, MAPE, MASE, and interval coverage;
- explain forecast uncertainty and prediction intervals;
- handle missing timestamps and irregular sampling;
- state when a global ML model is justified;
- communicate forecasts with assumptions and limitations.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| [Forecasting: Principles and Practice](https://otexts.com/fpp3/) (3rd ed., free) | Ch. **1–9** | Exploration, baselines, ETS, ARIMA, evaluation |
| FPP3 | Ch. **10–12** (selected) | Dynamic regression, hierarchical, advanced |
| [Hyndman & Athanasopoulos](https://robjhyndman.com/) blog/notes | Selected | Practical caveats |
| [Prophet docs](https://facebook.github.io/prophet/) or [statsmodels docs](https://www.statsmodels.org/) | ETS/ARIMA/state space | Implementation |
| [M5 competition guidance](https://www.kaggle.com/competitions/m5-forecasting-accuracy) | Selected | Hierarchical forecasting practice |
| [N-BEATS paper](https://arxiv.org/abs/1905.09435) or [TFT paper](https://arxiv.org/abs/1911.09070) | Full (one) | Neural forecasting context |

## Modules

1. **Time-series exploration** — frequency, trend, seasonality, cycles, autocorrelation, stationarity, structural breaks, missing data.
2. **Baselines** — mean, naive, seasonal naive, drift; why a complex model must beat them.
3. **Exponential smoothing** — simple, Holt, Holt-Winters, ETS; parameters and interpretation.
4. **ARIMA** — AR, MA, differencing, ACF/PACF, order selection, residual diagnostics, SARIMA.
5. **Features and ML** — lags, rolling statistics, calendar features, Fourier terms, target leakage, global vs local models.
6. **Evaluation and uncertainty** — rolling-origin backtesting, horizon-specific error, MASE, interval coverage, forecast reconciliation, communicating uncertainty.

## Labs

### Lab 1 — Exploration and baselines

Choose a public, non-sensitive time series. Plot it, decompose trend/seasonality, and build naive, seasonal-naive, and drift baselines. State the forecast horizon and why.

### Lab 2 — ETS and ARIMA

Fit ETS and ARIMA/SARIMA. Check residuals. Compare against baselines with a rolling-origin backtest. Explain one model-selection failure.

### Lab 3 — Feature-based ML

Build lag/rolling/calendar features with a temporal split. Train a gradient-boosted or linear model. Prove no future information leaks. Compare with the statistical models.

### Lab 4 — Uncertainty

Produce prediction intervals from one method. Evaluate empirical coverage on the backtest. Show a case where the intervals are too narrow and explain why.

### Lab 5 — Forecast memo

Write a decision-oriented forecast memo: data, horizon, method, backtest, uncertainty, assumptions, and what would invalidate the forecast. Include a dashboard or table of horizon-specific errors.

## Exercises

1. Identify trend and seasonality in a plot.
2. Compute a seasonal-naive forecast by hand.
3. Explain stationarity and differencing.
4. Read an ACF/PACF plot for a simple series.
5. Design a rolling-origin backtest.
6. Explain why random CV leaks in time series.
7. Compare MAE and RMSE for outlier sensitivity.
8. Explain MASE's advantage over MAPE.
9. Compute interval coverage.
10. State when hierarchical reconciliation is needed.

## Project increment (optional)

Add a time-series baseline and backtest to P7 using rolling-origin evaluation. Compare a seasonal naive model with one learned forecaster, report interval coverage, and document leakage risks. This is an elective extension, not a new ladder project.

## Exit check

- [ ] beat or explain failure to beat a seasonal-naive baseline;
- [ ] use a leakage-free temporal backtest;
- [ ] diagnose residuals or forecast errors;
- [ ] report horizon-specific accuracy and uncertainty;
- [ ] explain one structural-break limitation;
- [ ] write a decision-ready forecast memo.

## Common failure modes

- Random train/test splits for temporal data.
- Tuning on the test horizon.
- Using future values in lag features.
- Reporting MAPE with zeros or small values.
- Ignoring seasonality and trend.
- Treating prediction intervals as guaranteed.
- Assuming a global ML model is better without a baseline.

## Evidence to commit

- `labs/ai/AI19/` with exploration, baselines, ETS/ARIMA, ML features, interval evaluation, memo
- `notes/ai/AI19/summary.md`
- data source/license and forecast horizon record

## Optional depth

- *Time Series Analysis and Its Applications* (Shumway & Stoffer).
- *Deep Learning for Time Series Forecasting* (Brownlee).
- Hierarchical forecasting and reconciliation.
- Conformal prediction for time series.
- `sktime`, `statsforecast`, and `darts` docs.
