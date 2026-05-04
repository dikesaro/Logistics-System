import datetime
from typing import List, Dict, Tuple, Optional

class LogisticsCoordinator:
    def __init__(self):
        # Supplier data: {supplier_id: {"name": str, "reliability_score": float, "delivery_times": List[float], "quality_score": float}}
        self.suppliers: Dict[str, Dict] = {}

        # Logistics network: {location_id: {"name": str, "connections": List[Tuple[str, float]], "cost": float}}
        self.logistics_network: Dict[str, Dict] = {}

        # International partners: {partner_id: {"name": str, "location": str, "contact": str, "shipments": List[Dict]}}
        self.partners: Dict[str, Dict] = {}

        # Team members: {employee_id: {"name": str, "role": str, "performance": float, "mentoring_notes": str}}
        self.team: Dict[str, Dict] = {}

        # Performance metrics: List[Dict]
        self.performance_metrics: List[Dict] = []

        # Reports: List[Dict]
        self.reports: List[Dict] = []

    # --- Supplier Management ---
    def add_supplier(self, supplier_id: str, name: str) -> str:
        """Add a new supplier to the system."""
        if supplier_id not in self.suppliers:
            self.suppliers[supplier_id] = {
                "name": name,
                "reliability_score": 0.0,
                "delivery_times": [],
                "quality_score": 0.0
            }
            return f"Supplier {name} added with ID: {supplier_id}"
        return f"Supplier ID {supplier_id} already exists."

    def assess_supplier_performance(self, supplier_id: str, reliability_score: float, delivery_time: float, quality_score: float) -> str:
        """Assess and update supplier performance metrics."""
        if supplier_id in self.suppliers:
            supplier = self.suppliers[supplier_id]
            supplier["reliability_score"] = reliability_score
            supplier["delivery_times"].append(delivery_time)
            supplier["quality_score"] = quality_score
            avg_delivery_time = sum(supplier["delivery_times"]) / len(supplier["delivery_times"]) if supplier["delivery_times"] else 0
            return (
                f"Performance updated for {supplier['name']}:\n"
                f"  Reliability: {reliability_score}/100, "
                f"Avg. Delivery Time: {avg_delivery_time:.2f} days, "
                f"Quality: {quality_score}/100"
            )
        return f"Supplier ID {supplier_id} not found."

    def get_supplier_reliability_improvement(self, supplier_id: str) -> float:
        """Calculate the improvement in supplier reliability (simulated 20% improvement)."""
        if supplier_id in self.suppliers:
            return self.suppliers[supplier_id]["reliability_score"] * 1.20
        return 0.0

    # --- Logistics Network Optimization ---
    def add_location(self, location_id: str, name: str, cost: float) -> str:
        """Add a location to the logistics network."""
        if location_id not in self.logistics_network:
            self.logistics_network[location_id] = {
                "name": name,
                "connections": [],
                "cost": cost
            }
            return f"Location {name} added with ID: {location_id}"
        return f"Location ID {location_id} already exists."

    def add_connection(self, from_location: str, to_location: str, distance: float) -> str:
        """Add a connection between two locations in the network."""
        if from_location in self.logistics_network and to_location in self.logistics_network:
            self.logistics_network[from_location]["connections"].append((to_location, distance))
            self.logistics_network[to_location]["connections"].append((from_location, distance))
            return f"Connection added between {from_location} and {to_location}"
        return "One or both locations not found."

    def optimize_network(self) -> Dict:
        """Simulate network optimization (15% cost reduction)."""
        total_original_cost = sum(loc["cost"] for loc in self.logistics_network.values())
        optimized_cost = total_original_cost * 0.85  # 15% reduction
        return {
            "original_cost": total_original_cost,
            "optimized_cost": optimized_cost,
            "savings": total_original_cost - optimized_cost,
            "resilience_improvement": "Increased (simulated)"
        }

    # --- Partner Coordination ---
    def add_partner(self, partner_id: str, name: str, location: str, contact: str) -> str:
        """Add an international partner."""
        if partner_id not in self.partners:
            self.partners[partner_id] = {
                "name": name,
                "location": location,
                "contact": contact,
                "shipments": []
            }
            return f"Partner {name} added with ID: {partner_id}"
        return f"Partner ID {partner_id} already exists."

    def track_shipment(self, partner_id: str, shipment_id: str, status: str, lead_time: float) -> str:
        """Track a shipment with a partner and reduce lead times."""
        if partner_id in self.partners:
            self.partners[partner_id]["shipments"].append({
                "shipment_id": shipment_id,
                "status": status,
                "lead_time": lead_time,
                "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            return f"Shipment {shipment_id} tracked for {self.partners[partner_id]['name']}. Lead time: {lead_time} days"
        return f"Partner ID {partner_id} not found."

    # --- Team Management ---
    def add_team_member(self, employee_id: str, name: str, role: str) -> str:
        """Add a team member."""
        if employee_id not in self.team:
            self.team[employee_id] = {
                "name": name,
                "role": role,
                "performance": 0.0,
                "mentoring_notes": ""
            }
            return f"Team member {name} added with ID: {employee_id}"
        return f"Employee ID {employee_id} already exists."

    def update_team_performance(self, employee_id: str, performance: float, mentoring_notes: str = "") -> str:
        """Update team member performance and mentoring notes."""
        if employee_id in self.team:
            self.team[employee_id]["performance"] = performance
            self.team[employee_id]["mentoring_notes"] = mentoring_notes
            return f"Performance updated for {self.team[employee_id]['name']}: {performance}/100"
        return f"Employee ID {employee_id} not found."

    # --- Reporting ---
    def generate_report(self, report_id: str, title: str) -> Dict:
        """Generate a report summarizing key performance metrics and recommendations."""
        avg_supplier_reliability = (
            sum(sup["reliability_score"] for sup in self.suppliers.values()) / len(self.suppliers)
            if self.suppliers else 0
        )
        avg_lead_time = (
            sum(
                sum(ship["lead_time"] for ship in partner["shipments"])
                for partner in self.partners.values()
            ) / sum(len(partner["shipments"]) for partner in self.partners.values())
            if any(self.partners[pid]["shipments"] for pid in self.partners) else 0
        )
        avg_team_performance = (
            sum(emp["performance"] for emp in self.team.values()) / len(self.team)
            if self.team else 0
        )

        report = {
            "report_id": report_id,
            "title": title,
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "metrics": {
                "avg_supplier_reliability": avg_supplier_reliability,
                "avg_lead_time": avg_lead_time,
                "avg_team_performance": avg_team_performance,
                "network_optimization": self.optimize_network()
            },
            "recommendations": [
                "Conduct regular supplier performance reviews to maintain 20% reliability improvement.",
                "Expand logistics network optimization to additional regions for further cost savings.",
                "Implement real-time tracking with all international partners to reduce lead times.",
                "Schedule bi-weekly mentoring sessions to enhance team performance."
            ]
        }
        self.reports.append(report)
        return report

    def get_report(self, report_id: str) -> Optional[Dict]:
        """Retrieve a specific report by ID."""
        for report in self.reports:
            if report["report_id"] == report_id:
                return report
        return None

# --- Example Usage ---
if __name__ == "__main__":
    coordinator = LogisticsCoordinator()

    # Add suppliers and assess performance
    print(coordinator.add_supplier("S001", "Global Supplies Inc."))
    print(coordinator.assess_supplier_performance("S001", 85.0, 5.0, 90.0))
    print(f"Projected reliability improvement: {coordinator.get_supplier_reliability_improvement('S001'):.2f}")

    # Set up logistics network
    print(coordinator.add_location("L001", "New York Hub", 10000.0))
    print(coordinator.add_location("L002", "London Hub", 12000.0))
    print(coordinator.add_connection("L001", "L002", 3500.0))
    print("Network optimization results:", coordinator.optimize_network())

    # Add partners and track shipments
    print(coordinator.add_partner("P001", "EuroLogistics", "Berlin", "contact@eurologistics.com"))
    print(coordinator.track_shipment("P001", "SHIP123", "In Transit", 7.0))

    # Manage team
    print(coordinator.add_team_member("E001", "Alice Johnson", "Logistics Analyst"))
    print(coordinator.update_team_performance("E001", 92.0, "Needs advanced training in network modeling"))

    # Generate and print a report
    report = coordinator.generate_report("R001", "Q3 2026 Logistics Performance")
    print("\nGenerated Report:")
    for key, value in report.items():
        print(f"{key}: {value}")
