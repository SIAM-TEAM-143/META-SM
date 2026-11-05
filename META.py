#SM OK.BRO 

import platform

if platform.architecture()[0] != "64bit":
    print("32bit Not Supported!")
else:
    try:
        import metav10

        
        if hasattr(metav10, "main_menu"):
            metav10.main_menu()
        elif hasattr(metav10, "main"):
            metav10.main()
        else:
            print("Error:  function.")

    except Exception as e:
        import traceback
        print(f"\nCRITICAL ERROR: {e}")
        traceback.print_exc()
        input("\nPress Enter to exit...")
