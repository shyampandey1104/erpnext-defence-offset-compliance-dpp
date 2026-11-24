"""Defence Procurement Procedure (DAP 2020) Offset Banking & Compliance Engine."""
from dataclasses import dataclass, field
from datetime import datetime, date
from typing import List, Dict, Any, Optional

@dataclass
class DefenceOffsetContract:
    contract_id: str
    foreign_oem_name: str
    main_procurement_value_inr: float
    offset_obligation_pct: float       # e.g., 30% to 50%
    total_offset_target_inr: float = 0.0
    accumulated_banked_credits_inr: float = 0.0
    status: str = "ACTIVE"

@dataclass
class OffsetTransactionClaim:
    claim_id: str
    contract_id: str
    indian_offset_partner: str
    category: str                      # DIRECT_MANUFACTURING, MSME_TIER1, CRITICAL_TECH
    physical_value_inr: float
    applicable_multiplier: float = 1.0 # 1.5x for MSMEs, 2.0x for critical technology
    eligible_offset_credit_inr: float = 0.0

class DefenceOffsetComplianceEngine:
    def __init__(self, contract: DefenceOffsetContract):
        contract.total_offset_target_inr = round(contract.main_procurement_value_inr * (contract.offset_obligation_pct / 100.0), 2)
        self.contract = contract
        self.claims: Dict[str, OffsetTransactionClaim] = {}

    def submit_offset_transaction_claim(self, claim: OffsetTransactionClaim) -> Dict[str, Any]:
        claim.eligible_offset_credit_inr = round(claim.physical_value_inr * claim.applicable_multiplier, 2)
        self.claims[claim.claim_id] = claim
        self.contract.accumulated_banked_credits_inr = round(self.contract.accumulated_banked_credits_inr + claim.eligible_offset_credit_inr, 2)
        
        remaining_obligation = max(0.0, round(self.contract.total_offset_target_inr - self.contract.accumulated_banked_credits_inr, 2))
        return {
            "claim_id": claim.claim_id,
            "physical_value": claim.physical_value_inr,
            "multiplier_applied": claim.applicable_multiplier,
            "credit_banked_inr": claim.eligible_offset_credit_inr,
            "remaining_obligation_inr": remaining_obligation,
            "fulfillment_percentage": round((self.contract.accumulated_banked_credits_inr / self.contract.total_offset_target_inr) * 100.0, 2)
        }

    def evaluate_domw_annual_audit(self, current_period_year: int) -> Dict[str, Any]:
        fulfillment_pct = round((self.contract.accumulated_banked_credits_inr / self.contract.total_offset_target_inr) * 100.0, 2)
        is_compliant = fulfillment_pct >= 100.0
        
        # Penalties under DAP 2020: 5% of shortfall levied as Liquidated Damages (LD)
        shortfall = max(0.0, round(self.contract.total_offset_target_inr - self.contract.accumulated_banked_credits_inr, 2))
        potential_penalty = round(shortfall * 0.05, 2)

        return {
            "contract_id": self.contract.contract_id,
            "year": current_period_year,
            "target_inr": self.contract.total_offset_target_inr,
            "banked_credits_inr": self.contract.accumulated_banked_credits_inr,
            "fulfillment_pct": fulfillment_pct,
            "status": "OBLIGATION_FULFILLED" if is_compliant else "SHORTFALL_PENALTY_RISK",
            "liquidated_damages_exposure_inr": potential_penalty
        }
