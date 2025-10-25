import numpy as np

class PersonaAgent:
    def __init__(self, persona_data):
        self.id = persona_data.get('persona_id', 'N/A')
        self.attributes = persona_data.get('attributes', {})
        self.base_purchase_rate = persona_data.get('base_purchase_frequency_per_month', 0) / 30.0
        self.state = 'Unaware'
        self.p_churn = 0.05 

    def update_state(self, p_innovation, p_imitation, adoption_rate):
        if self.state == 'Unaware':
            prob_aware = p_innovation + p_imitation * adoption_rate
            if np.random.rand() < prob_aware:
                self.state = 'Active'
        elif self.state == 'Active':
            if np.random.rand() < self.p_churn:
                self.state = 'Churned'

    def attempt_purchase(self, month_modifier):
        if self.state == 'Active':
            monthly_purchase_prob = (1 - (1 - self.base_purchase_rate)**30) * month_modifier
            if np.random.rand() < monthly_purchase_prob:
                return 1
        return 0