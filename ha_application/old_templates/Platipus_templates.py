# Router Template
ROUTER_PROMT_TEMPLATE_VARS = ["input", "router_destenation_options"]
ROUTER_PROMT_TEMPLATE = """### Instruction:    
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
### RESPONSE:
"""

# Command Template
COMMAND_PROMT_IDENT_NAME = "DEVICE_COMMAND"
COMMAND_PROMT_DESCRIPTION = "Use if the user is trying to change the state of a smart home device."
COMMAND_PROMT_TEMPLATE_PRE_DEVICE = """### Instruction:    
Below is a "USER REQUEST" asking to make a change to a smart home device. Respond in JSON format as defined under "JSON STRUCTURE". 
All available devices and their alias are defined in the "DEVICE ALIAS LIST" in the format "Alias: device_id", choose the best fitting device. Also choose an "ACTION" from the "ACTION LIST". 
If multiple actions are required, list all devices and actions. You will also find a "HISTORY" for the last 5 "USER REQUESTS". If the user is referencing a previous request, use the appropiate devices from the "HISTORY" instead of the "DEVICE ALIAS LIST".
The "type" should always be "command".

JSON STRUCTURE: {{"type": "command", "commands": [{{"device": device_id, "action": action, "state": state}}]}}

ACTION LIST: power [STATE: on, off], dim [STATE: percentage], color [STATE: color name]

DEVICE ALIAS LIST:
"""
COMMAND_PROMT_TEMPLATE_POST_DEVICE = """

REMEMBER: Use the exact device Ids from the "DEVICE ALIAS LIST" or from "HISTORY". There might be gramatical errors in the Ids, so make sure to copy the Ids exactly including any errors.

HISTORY:
{chat_history}

USER REQUEST: "{input}"
### RESPONSE: 
"""

# Inquiry Template
INQUIRY_PROMT_IDENT_NAME = "DEVICE_INQUIRY"
INQUIRY_PROMT_DESCRIPTION = "Use if the user is requesting information about a smart home device"
INQUIRY_PROMT_TEMPLATE_PRE_DEVICE = """### Instruction:    
Below is a "USER REQUEST" asking to make get information about a smart home device. Respond in JSON format as defined under "JSON STRUCTURE". 
All available devices and their alias are defined in the "DEVICE ALIAS LIST" in the format "Alias: device_id", choose the best fitting device. Also choose an "attribute" from the "ATTRIBUTE LIST" that the user is asking about. 
If the user asks about multiple attributes or devices, list all devices and attributes. You will also find a "HISTORY" for the last 5 "USER REQUESTS". The "type" should always be "inquiry".

JSON STRUCTURE: {{"type": "inquiry", "commands": [{{"device": device_id, "attribute": string}}]}}

ATTRIBUTE LIST: state, brightness, color

DEVICE ALIAS LIST: 
"""
INQUIRY_PROMT_TEMPLATE_POST_DEVICE = """

REMEMBER: Use the exact device Ids from the "DEVICE ALIAS LIST" or from "HISTORY". There might be gramatical errors in the Ids, so make sure to copy the Ids exactly including any errors.

HISTORY:
{chat_history}

USER REQUEST: "{input}"
### RESPONSE:
"""

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
ASSISTANT ### RESPONSE:
"""

# conversation template
CONVERSATION_PROMPT_TEMPLATE = """### Instruction:    
You are a helpfull and friendly AI assistant connected to a smart home system. Your name is {AI_NAME} The user has just said something has nothing to do with the smart home system itself.

CONVERSATION HISTORY:
{chat_history}

USER: {input}
AI ASSISTANT ###RESPONSE:
"""