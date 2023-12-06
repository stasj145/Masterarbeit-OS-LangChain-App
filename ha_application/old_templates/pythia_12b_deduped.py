# Router Template
ROUTER_PROMT_TEMPLATE_VARS = ["input", "router_destenation_options"]
ROUTER_PROMT_TEMPLATE = """
### Instruction:    
Below are some "USER REQUESTS" and a "RESPONSE" from an AI assistant. The AI assistant is connected to a smart home system, so some USER REQUESTS might ask the assistant to interact with the smart home system. Respond in a JSON Markdown format as defined under "JSON STRUCTURE". Change the "destination" to one of the options provided under "DESTINATION OPTIONS". "next_inputs" Should always be an exact copy of the last USER REQUEST. 

JSON STRUCTURE: {{"destination": [DESTINATION OPTION], "next_inputs": [USER REQUEST]}}

DESTINATION OPTIONS:
{router_destenation_options}
DEFAULT: Usefull if the user is trying to make conversation and the request does not pertain to matters of the Smart Home system.

USER REQUEST: "set the lights in the example room to 50%"
RESPONSE: RESPONSE: {{"destination": "DEVICE_COMMAND", "next_inputs": "set the lights in the example room to 50%"}}

USER REQUEST: "Is the light in the Kitchen on?"
RESPONSE: {{"destination": "DEVICE_INQUIRY", "next_inputs": "Is the light in the Kitchen on?"}}

USER REQUEST: "Wrong room again... turn that light back off please! You ware supposed to change the color in the floor to a random color."
RESPONSE: {{"destination": "DEVICE_COMMAND", "next_inputs": "Wrong room again... turn that light back off please! You ware supposed to change the color in the floor to a random color."}}

USER REQUEST: "How are you?"
RESPONSE: {{"destination": "DEFAULT", "next_inputs": "How are you?"}}

USER REQUEST: "I am planing to bake a cake, but am unsure what kind i should make. Do you have any ideas?"
RESPONSE: {{"destination": "DEFAULT", "next_inputs": "I am planing to bake a cake, but am unsure what kind i should make. Do you have any ideas?"}}

USER REQUEST: "{input}"
### RESPONSE: """

# Command Template
COMMAND_PROMT_IDENT_NAME = "DEVICE_COMMAND"
COMMAND_PROMT_DESCRIPTION = "Use this destination if the USER REQUEST is trying to change the state of a smart home device. For example turning on a device."
COMMAND_PROMT_TEMPLATE_PRE_DEVICE = """
### Instruction:    
Below are "USER REQUESTS" and a "RESPONSE" from a Smart Home System. The "RESPONSE" always starts with "COMMAND:" followed by a JSON array as defined under "JSON STRUCTURE". 
The "DEVICE ALIAS LIST" lists all available devices in the format "Alias: device_ID", choose the best fitting device. Also choose an "ACTION" from the "ACTION LIST". 
If multiple actions are required, list all devices and actions. You will also find a "HISTORY" for the last interactions beween the user and the Smart Home System.

JSON STRUCTURE: [{{"DEVICE": device_ID, "ACTION": string, "STATE": string}}]

ACTION LIST: power [STATE], dim [STATE], color [STATE]

DEVICE ALIAS LIST:
Example Room: light.er, 
Main Example Room: light.main_exmpleR,
"""
COMMAND_PROMT_TEMPLATE_POST_DEVICE = """

REMEMBER: Use the exact device Ids from the "DEVICE ALIAS LIST". There might be gramatical errors in the Ids, so make sure to copy the Ids exactly.

USER REQUEST: "set the lights in the Example Room to 50%"
RESPONSE: COMMAND: [{{"DEVICE": "light.er", "ACTION": "dim", "STATE": "50"}}]

USER REQUEST: "Change the color in the Main Example Room to white and turn on the light in the Example room."
RESPONSE: COMMAND: [{{"DEVICE": "light.main_exmpleR", "ACTION": "color", "STATE": "white"}}, {{"DEVICE": "light.er", "ACTION": "power", "STATE": "on"}}]

USER REQUEST: "Turn on the example room light!"
RESPONSE: COMMAND: [{{"DEVICE": "light.er", "ACTION": "power", "STATE": "on"}}]

{chat_history}
USER REQUEST: "{input}"
### RESPONSE: """

# Inquiry Template
INQUIRY_PROMT_IDENT_NAME = "DEVICE_INQUIRY"
INQUIRY_PROMT_DESCRIPTION = "Use this destination if the USER REQUEST is trying to get information about the state of a smart home device"
INQUIRY_PROMT_TEMPLATE_PRE_DEVICE = """
### Instruction:    
Below are "USER REQUESTS" and a "RESPONSE" from a Smart Home System. The user is trying to gather information about a device. The Respons should be "INQUIRY: " followed by a JSON array as defined under "JSON STRUCTURE". 
The "DEVICE ALIAS LIST" lists all available devices in the format Alias: device_ID, choose the best fitting device. Also the "ATTRIBUTE" from the "ATTRIBUTE LIST" that the user is asking about. 
If the user asks about multiple attributes or devices, list all devices and attributes.

JSON STRUCTURE: [{{"DEVICE": device_ID, "ATTRIBUTE": string}}]

ATTRIBUTE: state, brightness, color

DEVICE ALIAS LIST: 
"""
INQUIRY_PROMT_TEMPLATE_POST_DEVICE = """

REMEMBER: Only use device ids from the "DEVICE ALIAS LIST". Never use a device that is not on that list!


USER REQUEST: "What brightness is the office light?"
RESPONSE: INQUIRY: [{{"DEVICE": "light.office", "ATTRIBUTE": "brightness"}}]

USER REQUEST: "Is the light in the Hallway on?"
RESPONSE: INQUIRY: [{{"DEVICE": "light.hallway", "ATTRIBUTE": "state"}}]

USER REQUEST: "What color is the light in the living room?."
RESPONSE: INQUIRY: [{{"DEVICE": "light.living_room", "ATTRIBUTE": "color"}}]

USER REQUEST: "What color is the light in the kitchen and is the bathroom light still on?"
RESPONSE: INQUIRY: [{{"DEVICE": "light.kitchen", "ATTRIBUTE": "color"}}, {{"DEVICE": "light.bathroom", "ATTRIBUTE": "state"}}]

{chat_history}
USER REQUEST: "{input}"
### RESPONSE: """

# Text Response Template
RESPONSE_PROMT_TEMPLATE= """### Instruction:    
You are a helpfull and friendly assistant connected to a smart home system. Under "SMART HOME SYSTEM:" you are given information from the smart home system. You should create a 1 to 2 scentence reply telling the user what the smart home did.

USER REQUEST:
Is the livingroom light on?
SMART HOME SYSTEM: 
[{{'DEVICE': 'light.living_room', 'ATTRIBUTE': 'state', 'STATE': 'off'}}]
ASSISTANT RESPONSE:
The livingroom light is currently off.

USER REQUEST:
What color is the kitchen light?
SMART HOME SYSTEM: 
[{{'DEVICE': 'light.kitchen', 'ATTRIBUTE': 'color', 'STATE': 'green'}}]
ASSISTANT RESPONSE:
The light in the kitchen is set to green.

USER REQUEST:
Is the livingroom light on and if so, what color is it?
SMART HOME SYSTEM: 
[{{'DEVICE': 'light.bathroom', 'ATTRIBUTE': 'state', 'STATE': 'on'}}, {{'DEVICE': 'light.bathroom', 'ATTRIBUTE': 'color', 'STATE': 'lime'}}]
ASSISTANT RESPONSE:
The Bathroom light is on and set to lime.

USER REQUEST:
Turn on the light in the livingroom and the kitchen!
SMART HOME SYSTEM: 
[{{"DEVICE": "light.living_room", "ACTION": "power", "STATE": "on"}}, {{"DEVICE": "light.kitchen", "ACTION": "power", "STATE": "on"}}]
ASSISTANT RESPONSE:
I turned on the light in the livingroom and the kitchen

USER REQUEST:
{user_request}
SMART HOME SYSTEM:
{smart_home_system}
ASSISTANT RESPONSE: """

# conversation template
CONVERSATION_PROMPT_TEMPLATE = """### Instruction:    
You are a helpfull and friendly AI assistant connected to a smart home system. Your name is {AI_NAME} The user has just said something has nothing to do with the smart home system itself.

CONVERSATION HISTORY:
{chat_history}

USER: {input}
AI ASSISTANT ###RESPONSE:
"""