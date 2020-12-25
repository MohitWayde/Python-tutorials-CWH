# 10-12-2020 to 11-12-2020
import re
mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +91 (20) 7235 8281
Fax: +91 (20) 7235 8727
91 (20) 7235 8723
91 (20) 7235 87211
91 (20) 7235 8727
91 (20) 7235 8726
91 (20) 7235 8725
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +91 (703) 243 9787
Fax: +91 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass '''
# for more info
# https://www.codewithharry.com/videos/python-tutorials-for-absolute-beginners-86
pat = re.compile(r"^fax")

match = pat.finditer(mystr)
print(match)
# for i in match:
#     print(i)

