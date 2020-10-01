# Creating the file
import pickle
result = []
with open("flights.dat",'wb') as file:
    while True:
        flight_number = int(input("enter flight number please: "))
        airline_name = input("enter airline name please: ")
        departure = (input("enter departure time: "))
        arrival = (input("enter time of arrival"))
        data = [flight_number, airline_name, departure, arrival]
        result.append(data)
        choice = input("continue? ").upper()
        if "N" in choice:
            break
    
with open("flights.dat", "wb") as f:
    pickle.dump(result, f)
    print("record addded :))")


#Checking for dubai 
with open("flights.dat",'rb') as f:
    details = pickle.load(f)
    for i in details:
        if i[2] == "Dubai":
            print(i)