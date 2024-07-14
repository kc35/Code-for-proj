import logic
 
if __names__ == '__main__':
     
    m = logic.start_game()
 
while(True):
 
    x = input("Press the command : ")

    if(x == 'W' or x == 'w'):
 
        m, flag_ = logic.move_up(m)
 
        status = logic.get_current_state(m)
        print(status)
 
        if(status == 'GAME NOT OVER'):
            logic.add_new_2(m)
 
        else:
            break
 
    elif(x == 'S' or x == 's'):
        m, flag_ = logic.move_down(m)
        status = logic.get_current_state(m)
        print(status)
        if(status == 'GAME NOT OVER'):
            logic.add_new_2(m)
        else:
            break
 
    elif(x == 'A' or x == 'a'):
        m, flag_ = logic.move_left(m)
        status = logic.get_current_state(m)
        print(status)
        if(status == 'GAME NOT OVER'):
            logic.add_new_2(m)
        else:
            break

    elif(x == 'D' or x == 'd'):
        m, flag_ = logic.move_right(m)
        status = logic.get_current_state(m)
        print(status)
        if(status == 'GAME NOT OVER'):
            logic.add_new_2(m)
        else:
            break
    else:
        print("Invalid Key Pressed")
      
    print(m)
