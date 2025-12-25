import os 
import CRUD as CRUD

if __name__ == "__main__":
  sistem_operasi = os.name
  
  match sistem_operasi:
    case "posix": os.system("clear")
    case "nt":os.system("cls")
  
  print("SELAMAT DATA DI PROGRAM")
  print("DATABASE PERPUSATKAAN")
  print("============================")
  
  # check database itu ada atau tidak
  CRUD.init_console()


  while(True):
    match sistem_operasi:
      case "posix": os.system("clear")
      case "nt":os.system("cls")

    print("SELAMAT DATA DI PROGRAM")
    print("DATABASE PERPUSATKAAN")
    print("============================")
      
    print(f"1.read data")
    print(f"2.create data")
    print(f"3.update data")
    print(f"4.delete data\n")

    user_option = input("Masukan Opsi: ")
    
    
    
    match user_option:
      case "1":CRUD.read_console()
      case "2":CRUD.create_console()
      case "3":CRUD.update_console()
      case "4":CRUD.delete_console()
      
    
    is_done = input("Apakah selesai (y/n)")
    if is_done == "y" or is_done == "Y":
      break
    
  print("Program berakhir")