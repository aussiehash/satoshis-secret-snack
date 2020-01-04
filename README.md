# Satoshis Secret Snack
Hardware and Software for creating a Bitcoin BIP39 seed, and then split it into a SLIP39 Shamir Secret Share. The Hardware is extremely inexpensive, and therefore 10 or even more of these can be created for $5-$10. You could probably make 100 for $25. 

![Alt text](img/make_pcb.gif?raw=true "Make PCB")
![Alt text](img/IMG_24.jpg?raw=true "Final Homemade PCBs")


## WARNING
This is an early stage project, and hasn't been thoroughly vetted. Happy Proof of Keys Day 2020, hopefully this project can get you thinking harder about your own Bitcoin security. It is also not fully complete, the step of generating the Shamir Share and writing to EEPROM isn't fully automated.

# Security Model
This device is meant to be a backup of a backup. You should still always have a Crypto-Steel or BillFodl, in a safe or somewhere ultra-secure, which will be your primary backup. Still if your apartment burns down, it might be less than ideal to actually retrieve the seed and do it quickly. Since these shares by themselves don't contain sensitive information, you can be slightly more loose with where you store them. Your car, work, relatives, etc. As long as you often audit the shares and make sure they haven't been tampered with, this can help give peace of mind about self-storing your Bitcoin.

## Shamir's Secret Sharing
Shamir's Secret Sharing is really useful because it stores your seed in pieces that are unusable and meaningless without enough of them to reach the targetted threshold (2/3),(3/5), or more. In addition, you might want full control over your funds, and you don't want to go to multiple locations just to send a transaction, like with a multi-sig setup. If all the pieces of your multi-sig are sitting in a drawer together somewhere, whats the point of the added hassle and increased fees?

# Hardware
1. EEPROM: CAT24C08WI-GT3 (Secret Storage)
1. Grove 4 Pin Header (I2C Header)
1. 330 Ohm Resistor 0805 (Input Filter)
1. 10uF 1208 Ceramic Capacitor (Input Filter)
1. 0.1uF Capacitor (EEPROM Decoupling)

Included are the PCB design files, which can be used for etching your own circuit board. In the attached GIF is a tuturial of how to make "tonor transfer PCBs".

# Software
Trezor's python-mnemonic (BIP39) and python-shamir-mnemonic (SLIP39)
