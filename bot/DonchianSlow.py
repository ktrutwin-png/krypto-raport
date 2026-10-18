# DonchianSlow - wolna strategia trendowa (long only) na 4h.
# Wejscie: zamkniecie wyzsze niz najwyzsze zamkniecie z ostatnich ~50 dni (300 swiec 4h).
# Wyjscie: zamkniecie nizsze niz najnizsze zamkniecie z ostatnich ~20 dni (120 swiec 4h).
# Zabezpieczenie: stoploss -20% (awaryjny). Brak dzwigni, brak shortow.
# Uwaga: logike przetestowano na DZIENNYCH danych BTC/EUR; wersja 4h jest jej odpowiednikiem
# i wymaga potwierdzenia backtestem.
from freqtrade.strategy import IStrategy
from pandas import DataFrame


class DonchianSlow(IStrategy):
    INTERFACE_VERSION = 3
    timeframe = "4h"
    can_short = False
    minimal_roi = {"0": 100}
    stoploss = -0.20
    trailing_stop = False
    process_only_new_candles = True
    startup_candle_count = 320
    use_exit_signal = True
    exit_profit_only = False

    entry_len = 300  # ~50 dni
    exit_len = 120   # ~20 dni

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["hi"] = dataframe["close"].rolling(self.entry_len).max().shift(1)
        dataframe["lo"] = dataframe["close"].rolling(self.exit_len).min().shift(1)
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (dataframe["close"] > dataframe["hi"]) & (dataframe["volume"] > 0),
            "enter_long",
        ] = 1
        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[dataframe["close"] < dataframe["lo"], "exit_long"] = 1
        return dataframe
