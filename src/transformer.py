import pandas as pd

def transform_data(df: pd.DataFrame) -> dict:
    """
    Transforms the cleaned data into analytics.
    Returns a dict where every key is a DataFrame for the dashboard.
    """

    # 1) Fraud rate per merchant
    fraud_rate_merchant = (
        df.groupby("merchant")["is_fraud"]
        .mean()
        .reset_index()
        .rename(columns={"is_fraud": "fraud_rate"})
        .sort_values("fraud_rate", ascending=False)
    )

    # 2) Fraud rate per category
    fraud_rate_category = (
        df.groupby("category")["is_fraud"]
        .mean()
        .reset_index()
        .rename(columns={"is_fraud": "fraud_rate"})
        .sort_values("fraud_rate", ascending=False)
    )

    # 3) Daily summary (sum, mean, count, fraud rate)
    daily_summary = (
        df.groupby("trans_date")
        .agg({
            "amt": ["sum", "mean"],
            "is_fraud": "mean",
            "merchant": "count"
        })
        .reset_index()
    )
    daily_summary.columns = ["trans_date", "total_amt", "avg_amt", "fraud_rate", "transaction_count"]

    # 4) Merchant-level summary (sum, mean, count, fraud rate)
    merchant_summary = (
        df.groupby("merchant")
        .agg({
            "amt": ["sum", "mean"],
            "is_fraud": "mean",
            "category": "count"
        })
        .reset_index()
    )
    merchant_summary.columns = ["merchant", "total_amt", "avg_amt", "fraud_rate", "transaction_count"]

    # 5) Category-level summary
    category_summary = (
        df.groupby("category")
        .agg({
            "amt": ["sum", "mean"],
            "is_fraud": "mean",
            "merchant": "count"
        })
        .reset_index()
    )
    category_summary.columns = ["category", "total_amt", "avg_amt", "fraud_rate", "transaction_count"]

    # 6) Top merchants by fraud
    top_fraud_merchants = fraud_rate_merchant.head(10)

    # 7) Top merchants by revenue
    top_revenue_merchants = merchant_summary.sort_values("total_amt", ascending=False).head(10)

    # Return all analytics in a dict
    return {
        "fraud_rate_merchant": fraud_rate_merchant,
        "fraud_rate_category": fraud_rate_category,
        "daily_summary": daily_summary,
        "merchant_summary": merchant_summary,
        "category_summary": category_summary,
        "top_fraud_merchants": top_fraud_merchants,
        "top_revenue_merchants": top_revenue_merchants
    }



