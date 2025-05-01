
reg_input = input()
ID_mode = input()

if reg_input.startswith("0b"):  # Binário
    reg = int(reg_input, 2)
    
elif reg_input.startswith("0x"):  # Hexadecimal
    reg = int(reg_input, 16)
    
else:  # Decimal
    reg = int(reg_input)
    
power_on = "Yes" if reg & (1 << 0) else "No"
error    = "Yes" if reg & (1 << 1) else "No"
ready    = "Yes" if reg & (1 << 2) else "No"
overheat = "Yes" if reg & (1 << 3) else "No"
    
print("===========================")
print("      REGISTER STATE       ")
print("===========================")
print(f"  Power On    : {power_on}")
print(f"  Error       : {error}")
print(f"  Ready       : {ready}")
print(f"  Overheat    : {overheat}")
print(f"  Mode ID     : {ID_mode}")