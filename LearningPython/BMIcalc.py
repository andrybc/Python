
weight = float(input("How much do you weigh?: "))
weight_units = str(input("Is this in Lbs(L) or Kgs(K)?: "))

height = str(input("How tall are you?: "))
height_units = str(input("Is this in Feet and inches(F) or Meters(M)?: "))

if weight_units == "L":
    weight*= 0.45
    weight_units = "K"
if height_units == "F":
    apost = height.find("'")
    height_in_meters = float(height[apost-1])*0.3048
   # print(height_in_meters)
    height_in_meters += float(height[apost+1:])*0.0254
   # print(height_in_meters)
    height = str(height_in_meters)

weight = round(weight,2)
height = round(float(height),2)

BMI = weight/(float(height)**2)
print("Your BMI is ", round(BMI,2))

if BMI >=25:
    print("You are overweight")
elif BMI<25 and BMI >=18.5:
    print("You are normal weight")
else:
    print("You are underweight")