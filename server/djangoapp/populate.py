from .models import CarMake, CarModel

def initiate():
    print("=== initiate function called ===")
    
    # First delete any existing data to avoid duplicates
    CarModel.objects.all().delete()
    CarMake.objects.all().delete()
    print("Cleared existing data")
    
    car_make_data = [
        {"name":"NISSAN", "description":"Great cars. Japanese technology"},
        {"name":"Mercedes", "description":"Great cars. German technology"},
        {"name":"Audi", "description":"Great cars. German technology"},
        {"name":"Kia", "description":"Great cars. Korean technology"},
        {"name":"Toyota", "description":"Great cars. Japanese technology"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make = CarMake.objects.create(name=data['name'], description=data['description'])
        car_make_instances.append(car_make)
        print(f"Created CarMake: {car_make.name}")

    print(f"Created {len(car_make_instances)} car makes")

    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
      {"name":"Pathfinder", "type":"SUV", "year": 2023, "car_make":car_make_instances[0], "dealer_id": 1},
      {"name":"Qashqai", "type":"SUV", "year": 2023, "car_make":car_make_instances[0], "dealer_id": 1},
      {"name":"XTRAIL", "type":"SUV", "year": 2023, "car_make":car_make_instances[0], "dealer_id": 1},
      {"name":"A-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1], "dealer_id": 2},
      {"name":"C-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1], "dealer_id": 2},
      {"name":"E-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1], "dealer_id": 2},
      {"name":"A4", "type":"SUV", "year": 2023, "car_make":car_make_instances[2], "dealer_id": 3},
      {"name":"A5", "type":"SUV", "year": 2023, "car_make":car_make_instances[2], "dealer_id": 3},
      {"name":"A6", "type":"SUV", "year": 2023, "car_make":car_make_instances[2], "dealer_id": 3},
      {"name":"Sorrento", "type":"SUV", "year": 2023, "car_make":car_make_instances[3], "dealer_id": 4},
      {"name":"Carnival", "type":"SUV", "year": 2023, "car_make":car_make_instances[3], "dealer_id": 4},
      {"name":"Cerato", "type":"Sedan", "year": 2023, "car_make":car_make_instances[3], "dealer_id": 4},
      {"name":"Corolla", "type":"Sedan", "year": 2023, "car_make":car_make_instances[4], "dealer_id": 5},
      {"name":"Camry", "type":"Sedan", "year": 2023, "car_make":car_make_instances[4], "dealer_id": 5},
      {"name":"Kluger", "type":"SUV", "year": 2023, "car_make":car_make_instances[4], "dealer_id": 5},
    ]

    for data in car_model_data:
        car_model = CarModel.objects.create(
            name=data['name'], 
            car_make=data['car_make'], 
            type=data['type'], 
            year=data['year'],
            dealer_id=data['dealer_id']  # Make sure this line is included
        )
        print(f"Created CarModel: {car_model.car_make.name} {car_model.name}")
    
    final_car_make_count = CarMake.objects.count()
    final_car_model_count = CarModel.objects.count()
    print(f"=== Initiate complete: {final_car_make_count} car makes, {final_car_model_count} car models ===")