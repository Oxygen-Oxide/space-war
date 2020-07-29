import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="space war",
    options={"build_exe": {"packages":["pygame","math","random"],
                           "include_files":['backimg.png','background.wav','transport.png','gaming.png','enemy.png','bullet.png','stilo.ttf','laser.wav','explosion.wav']}},
    executables = executables

    )
