from .agents import PersonaAgent
import numpy as np
import logging

class MarketSimulation:
    def __init__(self, personas, tam, market_share, modifiers, initial_adoption_rate=0.1):
        self.agents = [PersonaAgent(p) for p in personas if p]
        self.potential_market_size = int(tam * market_share)
        self.modifiers = modifiers
        self.p_innovation = 0.01
        self.q_imitation = 0.38
        
        num_initial_adopters = int(len(self.agents) * initial_adoption_rate)
        np.random.shuffle(self.agents)
        for i in range(num_initial_adopters):
            if i < len(self.agents):
                self.agents[i].state = 'Active'
                
        self.adopters = int(self.potential_market_size * initial_adoption_rate)
        logging.info(f" - Simulation started, initial adoption rate: {initial_adoption_rate*100:.1f}%, estimated active customers: {self.adopters}")

    def run_simulation(self, months=12):
        monthly_sales_results = []
        num_agents = len(self.agents)
        if num_agents == 0:
            logging.warning(" [ERROR] No agents available for simulation. Returning zeros.")
            return [0] * months

        for month_index in range(months):
            adoption_rate = self.adopters / self.potential_market_size if self.potential_market_size > 0 else 0
            current_month_sales = 0
            active_agents_count = 0
            
            for agent in self.agents:
                agent.update_state(self.p_innovation, self.q_imitation, adoption_rate)
                month_modifier = self.modifiers[month_index]
                current_month_sales += agent.attempt_purchase(month_modifier)
                if agent.state == 'Active':
                    active_agents_count += 1
            
            sample_purchase_rate = current_month_sales / num_agents if num_agents > 0 else 0
            extrapolated_sales = sample_purchase_rate * self.potential_market_size
            monthly_sales_results.append(int(extrapolated_sales))
            
            self.adopters = (active_agents_count / num_agents) * self.potential_market_size if num_agents > 0 else 0
            
        return monthly_sales_results