base_input = float(input("Anna suorakulmion kanta (cm): "))
height_input = float(input("Anna suorakulmion korkeus (cm): "))
rectangle_perimeter = base_input * 2 + height_input * 2
rectangle_area = base_input * height_input
print(f"\nSuorakulmion piiri on {rectangle_perimeter:.2f}cm, pinta-ala on {rectangle_area:.2f}cm")
