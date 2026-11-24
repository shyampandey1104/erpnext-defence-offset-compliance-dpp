import unittest
from defence_offset_compliance.engine import DefenceOffsetContract, OffsetTransactionClaim, DefenceOffsetComplianceEngine

class TestDefenceOffsetComplianceEngine(unittest.TestCase):
    def setUp(self):
        contract = DefenceOffsetContract(
            contract_id="DEF-MOD-2026-FIGHTER-01", foreign_oem_name="Dassault Aviation",
            main_procurement_value_inr=10000000000.0, offset_obligation_pct=30.0
        )
        self.engine = DefenceOffsetComplianceEngine(contract)

    def test_offset_multiplier_credit_banking(self):
        claim = OffsetTransactionClaim(
            claim_id="CLAIM-DOMW-001", contract_id="DEF-MOD-2026-FIGHTER-01",
            indian_offset_partner="Bharat Forge Defence", category="MSME_TIER1",
            physical_value_inr=1000000000.0, applicable_multiplier=1.5
        )
        res = self.engine.submit_offset_transaction_claim(claim)
        self.assertEqual(res["credit_banked_inr"], 1500000000.0) # 100Cr * 1.5 = 150Cr
        self.assertEqual(res["fulfillment_percentage"], 50.0)

    def test_domw_audit_penalty_exposure(self):
        audit = self.engine.evaluate_domw_annual_audit(2026)
        self.assertGreater(audit["liquidated_damages_exposure_inr"], 0)
        self.assertEqual(audit["status"], "SHORTFALL_PENALTY_RISK")

if __name__ == "__main__":
    unittest.main()
