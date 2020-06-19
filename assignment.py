# Exercise 2
# Agent selector

import random

# Class to create the agents.
class agent:

	def __init__(self, name, is_available, available_since, roles):
		self.name = name
		self.is_available = is_available
		self.available_since = available_since
		self.roles = roles

# Class for all the selection methods
class agent_selection_mode:

	# Method to forward issue to all available agents.
	def all_available(self, agents, issue):

		forward_to = []

		for agent in agents:
			if agent.is_available:
				if all(item in agent.roles for item in issue): # Cheking if agent have all the roles for issue
					forward_to.append(agent.name)

		if forward_to:
			return forward_to
		else:
			return 'No agents available'

	# Method to forward issue to least busy agent
	def least_busy(self, agents, issue):

		available_list = {}

		for agent in agents:
			if agent.is_available:
				if all(item in agent.roles for item in issue):# Cheking if agent have all the roles for issue.
					available_list.update({agent.name : agent.available_since})

		if available_list:
			least_busy = max(available_list, key=available_list.get)# Getting the agent that is least busy.
			return least_busy
		else:
			return 'No agents available'

	# Method to forward issue to random agent
	def random_mode(self, agents, issue):
		
		available_list = []

		for agent in agents:
			if agent.is_available:
				if all(item in agent.roles for item in issue):# Cheking if agent have all the roles for issue.
					available_list.append(agent.name)

		if available_list:
			selected_agent = random.choice(available_list)# Making random guess for agent.
			return selected_agent
		else:
			return 'No agents available'


# List of agents
agents = [
	agent('Mark', True, 2, ['sales' , 'support']),
	agent('Josh', False, 0, ['sales' , 'support']),
	agent('Joy', True, 3, ['speaker' , 'support']),
	agent('Mosh', True, 3, ['support' , 'sales']),
	agent('Siri', True, 4, ['speaker' , 'support'])
]

# Taking the issues from user and converting into list
issue = input("Enter the issues (Enter space between two issues) : ").split()

print('Select the mode below')
print('1 All available')
print('2 least busy')
print('3 Random mode')
choice = int(input())

# Making instance of selection mode class
mode = agent_selection_mode()

if choice == 1:
	print(mode.all_available(agents, issue))
elif choice == 2:
	print(mode.least_busy(agents, issue))
elif choice == 3:
	print(mode.random_mode(agents, issue))
else:
	print('Enter a valid input.')
	