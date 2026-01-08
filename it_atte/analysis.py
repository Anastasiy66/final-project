import pandas as pd
import matplotlib.pyplot as plt

def operations_to_df(operations: list) -> pd.DataFrame:
    """Преобразование в DataFrame"""
    df = pd.DataFrame([op.to_dict() for op in operations])
    if not df.empty:
        df["date"] = pd.to_datetime(df["date"])
    return df

def group_by_category(df: pd.DataFrame, op_type: str) -> pd.Series:
    """Группировка по категории для заданного типа травматизма"""
    filtered = df[df["op_type"] == op_type]
    return filtered.groupby("category")["amount"].sum()

def plot_pie_by_category(df: pd.DataFrame, op_type: str):
    """Круговая диаграмма прострадавших при  легких и тяжелых несчастных случаях """
    data = group_by_category(df, op_type)
    if data.empty:
        print(f"Нет данных для {op_type}")
        return
    data.plot(kind="pie", autopct="%1.1f%%", figsize=(6,6), title=f"{op_type.capitalize()} по категориям")
    plt.ylabel("")
    plt.show()


