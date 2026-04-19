#Undone 
import os

class Installed_Antivirus:
    def __init__(self):
        pass

    def print_av(self):
        antivirus = {
            'Windows Defender': 'C:\\ProgramData\\Microsoft\\Windows Defender',
            'Malwarebytes': 'C:\\Program Files\\Malwarebytes',
            'Bitdefender': 'C:\\Program Files\\Bitdefender',
            'Norton Security': 'C:\\Program Files\\Norton Security',
            'Norton Security (x86)': 'C:\\Program Files (x86)\\Norton Security',
            'McAfee': 'C:\\Program Files\\McAfee',
            'TotalAV': 'C:\\Program Files (x86)\\TotalAV',
            'CESET': 'C:\\Program Files\\ESET\\ESET Security',
            'Avira': 'C:\\Program Files (x86)\\Avira',
            'Surfshark': 'C:\\Program Files\\Surfshark',
            'Kaspersky': 'C:\\Program Files (x86)\\Kaspersky Lab',
            'Kaspersky (32Bit)': 'C:\\Program Files\\Kaspersky Lab',
            'Aura': 'C:\\Program Files\\Aura',
            'PIA Antivirus': ' C:\\Program Files\\Private Internet Access',
            'Avast': 'C:\\Program Files\\Avast Software\\Avast',
            'AVG': 'C:\\Program Files\\AVG\\Antivirus',
            'Webroot': 'C:\\Program Files\\Webroot',
            'Webroot (x86)': 'C:\\Program Files (x86)\\ Webroot',
            'BullGuard': 'C:\\Program Files\\BullGuard Ltd\\BullGuard',
            'Sophos': 'C:\\Program Files\\Sophos',
            'Sophos (x86)': 'C:\\Program Files (x86)\\Sophos'
        }

        installed_antivirus = []

        for name in antivirus:
            if os.path.exists(antivirus[name]):
                installed_antivirus.append(name)

        return installed_antivirus


clear_list = Installed_Antivirus()
print("".join(clear_list.print_av()))
