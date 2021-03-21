username=input("enter username ")    #input username
password=input("enter password ")    #input password

if username=="hotel_manager" and password=="ht_mg@123":              #checking autherisation
    
    
    staff={1:"anu",2:"bhagya",3:"dev",4:"raj",5:"simran"}
    rooms={10:"available",20:"available",30:"available",40:"available",50:"available",60:"available",70:"available",80:"available"}


    while(True):
        
        menu=input("""enter
            1. see currently available rooms
            2. see the staff list
            3. search for staff with name
            4. search staff with id
            5. book rooms with id
            6. make rooms available
            7. exit\n""")

        #1
        def availrooms(rooms):
            for x in rooms:
                print(x,rooms[x])

        #2
        def staffwork(staff):
            print("the working staff is")
            for x in staff:
                print(x,staff[x])

        #3
        def searchstaff(s):
            if s in staff.values():
                print("this staff works in our hotel")
            else:
                print("this staff doesn't work in our hotel")

        #4
        def search_id(sid):
            if sid in staff.keys():
                print("this staff does work here and their name is",staff[sid])
            else:
                print("this staff doesn't work here")

        #5
        def room_book(roomid):
            if roomid in rooms.keys():
                rooms[roomid]="unavailable"
                for x in rooms:
                    print(x,rooms[x])
            else:
                print("this room id doesn't exist")

        #6
        def emty_room(rid):
            if rid in rooms.keys():
                rooms[rid]="available"
                for x in rooms:
                    print(x,rooms[x])

        if menu=='1':
            availrooms(rooms)
        elif menu=='2':
            staffwork(staff)
        elif menu=='3':
            s=input("enter the name of staff ")
            searchstaff(s)
        elif menu=='4':
            sid=int(input("enter the id of the staff "))
            search_id(sid)
        elif menu=='5':
            roomid=int(input("enter the id of the room to book "))
            room_book(roomid)
        elif menu=='6':
            rid=int(input("enter the id of the room to make it available "))
            emty_room(rid)
        elif menu=='7':
            break
        else:
            print("enter valid input")

else:
    print("unauthorised access")