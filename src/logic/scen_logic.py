SCN_CASH_001={
  "aml_scenario_id": "SCN_CASH_001",
  "aml_scenario_name": "Significant Cash Activity",
  "scenario_description": "Detects cash activity above policy thresholds and patterns suggestive of structuring to avoid reporting requirements.",
  "scenario_logic": {
    "evaluation_window": "24_hours",
    "aggregation_level": "customer",
    "trigger_operator": "ANY",
    "trigger_description": "Generate an alert when one or more cash-activity rules are met within the evaluation window.",
    "rules": [
      { "rule_id": "TOTAL_CASH", "metric": "total_cash_activity", "operator": ">=", "threshold_name": "cash_activity_in_24_hours" },
      { "rule_id": "CASH_DEPOSIT", "metric": "total_cash_deposit", "operator": ">=", "threshold_name": "cash_deposit_in_24_hours" },
      { "rule_id": "CASH_WITHDRAWAL", "metric": "total_cash_withdrawal", "operator": ">=", "threshold_name": "cash_withdrawal_in_24_hours" },
      { "rule_id": "STRUCTURING_COUNT", "metric": "cash_transaction_count", "operator": ">=", "threshold_name": "cash_transaction_count_in_24_hours" }
    ]
  }
}

SCN_GEO_001={
  "aml_scenario_id": "SCN_GEO_001",
  "aml_scenario_name": "High-Risk Geography Transactions",
  "scenario_description": "Detects transfers to or from jurisdictions classified as high risk by the institution or applicable AML controls.",
  "scenario_logic": {
    "evaluation_window": "30_days",
    "aggregation_level": "customer_and_country",
    "trigger_operator": "ANY",
    "trigger_description": "Only transactions linked to a country with a risk score at or above the configured limit are assessed. Generate an alert when one or more rules are met.",
    "rules": [
      { "rule_id": "COUNTRY_RISK", "metric": "country_risk_score", "operator": ">=", "threshold_name": "high_risk_geo_country_risk_score" },
      { "rule_id": "TRANSFER_VALUE", "metric": "total_high_risk_geo_transfer_value", "operator": ">=", "threshold_name": "high_risk_geo_transfer_value" },
      { "rule_id": "TRANSFER_COUNT", "metric": "high_risk_geo_transaction_count", "operator": ">=", "threshold_name": "high_risk_geo_transaction_count" },
      { "rule_id": "SINGLE_TRANSFER", "metric": "max_high_risk_geo_transfer_value", "operator": ">=", "threshold_name": "single_high_risk_geo_transfer" }
    ]
  }
}

SCN_RMM_001={
  "aml_scenario_id": "SCN_RMM_001",
  "aml_scenario_name": "Rapid Movement of Money",
  "scenario_description": "Detects quick movement of recently credited funds through outgoing payments, transfers, or withdrawals.",
  "scenario_logic": {
    "evaluation_window": "48_hours",
    "aggregation_level": "customer_and_credit",
    "trigger_operator": "ALL",
    "trigger_description": "Generate an alert only when the movement amount, percentage moved, elapsed time, and transaction count rules are all met for a credited amount.",
    "rules": [
      { "rule_id": "MOVED_AMOUNT", "metric": "funds_moved_value", "operator": ">=", "threshold_name": "funds_moved_within_48_hours" },
      { "rule_id": "MOVED_PERCENTAGE", "metric": "funds_moved_percentage", "operator": ">=", "threshold_name": "funds_moved_percentage" },
      { "rule_id": "ELAPSED_TIME", "metric": "elapsed_hours", "operator": "<=", "threshold_name": "rapid_movement_elapsed_hours" },
      { "rule_id": "MOVEMENT_COUNT", "metric": "outgoing_transaction_count", "operator": ">=", "threshold_name": "rapid_movement_transaction_count" }
    ]
  }
}

SCN_TRADE_001={
  "aml_scenario_id": "SCN_TRADE_001",
  "aml_scenario_name": "Unusual Trade Activity",
  "scenario_description": "Detects unusually large, frequent, or structurally inconsistent trade transactions compared with the customer profile and historical activity.",
  "scenario_logic": {
    "evaluation_window": "30_days",
    "aggregation_level": "customer",
    "trigger_operator": "ANY",
    "trigger_description": "Generate an alert when one or more rules are met within the evaluation window.",
    "rules": [
      { "rule_id": "TRADE_VALUE", "metric": "total_trade_value", "operator": ">=", "threshold_name": "trade_value_in_30_days" },
      { "rule_id": "TRADE_COUNT", "metric": "trade_count", "operator": ">=", "threshold_name": "trade_count_in_30_days" },
      { "rule_id": "SINGLE_TRADE", "metric": "max_single_trade_value", "operator": ">=", "threshold_name": "single_trade_value" },
      { "rule_id": "BASELINE_DEVIATION", "metric": "trade_value_deviation_pct", "operator": ">=", "threshold_name": "trade_value_deviation_pct" }
    ]
  }
}

SCN_TXN_001={
  "aml_scenario_id": "SCN_TXN_001",
  "aml_scenario_name": "Unusual Transaction Activity",
  "scenario_description": "Detects abnormal credits, debits, transaction counts, or counterparties compared with the customer baseline.",
  "scenario_logic": {
    "evaluation_window": "7_days",
    "aggregation_level": "customer",
    "trigger_operator": "ANY",
    "trigger_description": "Generate an alert when one or more rules are met within the evaluation window.",
    "rules": [
      { "rule_id": "VOLUME", "metric": "total_transaction_volume", "operator": ">=", "threshold_name": "transaction_volume_in_7_days" },
      { "rule_id": "COUNT", "metric": "total_transaction_count", "operator": ">=", "threshold_name": "transaction_count_in_7_days" },
      { "rule_id": "SINGLE_TRANSACTION", "metric": "max_single_transaction_value", "operator": ">=", "threshold_name": "single_transaction_value" },
      { "rule_id": "BASELINE_DEVIATION", "metric": "transaction_volume_deviation_pct", "operator": ">=", "threshold_name": "transaction_volume_deviation_pct" }
    ]
  }
}

scen_logic_by_id = {
    "SCN_CASH_001": SCN_CASH_001["scenario_logic"],
    "SCN_GEO_001": SCN_GEO_001["scenario_logic"],
    "SCN_RMM_001": SCN_RMM_001["scenario_logic"],
    "SCN_TRADE_001": SCN_TRADE_001["scenario_logic"],
    "SCN_TXN_001": SCN_TXN_001["scenario_logic"]
}

def get_scen_logic(scenario_id:str):
    scenario_logic = scen_logic_by_id.get(scenario_id)
    if scenario_logic is None:
        raise ValueError(
            f"Scenario logic not configured: {scenario_id}"
        )
    return scenario_logic
