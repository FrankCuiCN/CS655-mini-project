# CS655-mini-project

# Image Recognition Application

## Links to Demo Videos
Video 1: https://drive.google.com/file/d/14Yx-NWZN2MqbP07yjwNoRoabB51KUVtG/view?usp=sharing

Video 2: https://drive.google.com/file/d/1YrdVsfMoM6dbHeB5bG8GJoGrAyoMgrLg/view?usp=sharing

## How to run

**Step 1:** download ```mini-project-C-M_request_rspec.xml```. Create a GENI resource using this RSpec file after selecting an InstaGENI site

**Step 2:** SSH into ```Web-interface``` and run```git clone https://github.com/FrankCuiCN/CS655-mini-project```

**Step 3:** Run ```cd CS655-mini-project```, and run ```chmod +x ./set_up_web_interface.sh```

**Step 4:** Execute ```./set_up_web_interface.sh``` (Rarely you have to press Enter or Y)

**Step 5:** SSH into ```Server``` and run ```git clone https://github.com/FrankCuiCN/CS655-mini-project```

**Step 6:** Run ```cd CS655-mini-project```, and run ```chmod +x ./set_up_backend.sh```

**Step 7:** Execute ```./set_up_backend.sh``` (Rarely you have to press Enter or Y)

**Step 8:** On ```Server```, ```run python3 ./server_base.py```

**Step 9:** Use our application by visiting ```IP/web_interface.html``` or ```IP/udp_web_interface.html```, where ```IP``` is the ip address of your ```Web-interface``` node.
