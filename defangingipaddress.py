#address = "1.1.1.1"
#"1[.]1[.]1[.]1"
def defangIPaddr( address: str) -> str:
        s=""
        address=address.replace('.','[.]')
        return address
print(defangIPaddr("1.1.1.1"))