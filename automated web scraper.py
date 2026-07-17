import requests
from bs4 import BeautifulSoup
url = requests.get("https://www.amazon.com/adidas-Unisex-Adult-Soccer-Indigo-Metallic/dp/B0DJWP8Y8T/?_encoding=UTF8&pd_rd_w=SwGSA&content-id=amzn1.sym.9929d3ab-edb7-4ef5-a232-26d90f828fa5&pf_rd_p=9929d3ab-edb7-4ef5-a232-26d90f828fa5&pf_rd_r=SC4BSNV9SK4VQ9TJSF8C&pd_rd_wg=Gi6kg&pd_rd_r=df276b18-b386-4bc5-803b-620d169eed00&ref_=pd_hp_d_btf_crs_zg_bs_3375251&th=1")
print(url.status_code)
print(url.json())
# Extraction script
# Import core modules 

# Download Page content

# Parse Raw HTML 

# Export Data to a structured File

# Open Document File

# Automate schedule