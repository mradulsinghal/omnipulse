"""Engagement Velocity Scorer for Multi-Platform Social Ingestion."""
import math
from typing import Dict, Any, List

class EngagementScorer:
    """Decay-Adjusted Engagement Velocity Scorer."""
    
    @staticmethod
    def calculate_velocity(likes: int, comments: int, reposts: int = 0, age_hours: float = 1.0) -> float:
        """
        EV = (Likes + 2.5*Comments + 4.0*Reposts) / (Age_Hours + 0.5)^1.2
        """
        raw = likes + (2.5 * comments) + (4.0 * reposts)
        time_penalty = math.pow(max(age_hours, 0.1) + 0.5, 1.2)
        return round(raw / time_penalty, 2)

    @classmethod
    def rank_items(cls, items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        for item in items:
            likes = int(item.get("likes", item.get("score", 0)))
            comments = int(item.get("comments", 0))
            reposts = int(item.get("reposts", item.get("retweets", 0)))
            age = float(item.get("age_hours", 4.0))
            item["velocity_score"] = cls.calculate_velocity(likes, comments, reposts, age)
        return sorted(items, key=lambda x: x.get("velocity_score", 0), reverse=True)
