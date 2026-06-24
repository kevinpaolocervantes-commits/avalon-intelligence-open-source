class AdversarialAgent:
    """
    Challenges a recommendation before action.
    """

    def review(self, recommendation: dict) -> dict:
        thesis = recommendation.get("thesis", "")
        confidence = recommendation.get("confidence", 0)
        evidence = recommendation.get("supporting_evidence", [])

        risks = []

        if confidence > 80:
            risks.append("Confidence may be too high. Check for overfitting or missing context.")

        if len(evidence) < 3:
            risks.append("Recommendation may be under-supported. More evidence is needed.")

        if "assumption" not in thesis.lower():
            risks.append("Key assumptions are not clearly stated.")

        return {
            "agent": "Adversarial Agent",
            "status": "review_complete",
            "risks_identified": risks,
            "challenge": "Proceed only if the recommendation survives uncertainty, missing data, and opposing evidence."
        }
