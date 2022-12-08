# CS655-mini-project

# Image Recognition Application

## Links to Demo Videos
Video 1: https://drive.google.com/file/d/14Yx-NWZN2MqbP07yjwNoRoabB51KUVtG/view?usp=sharing

Video 2: https://drive.google.com/file/d/1YrdVsfMoM6dbHeB5bG8GJoGrAyoMgrLg/view?usp=sharing

## How to run

**Step 1:** download mini-project-C-M_request_rspec.xml, and create a GENI resource using this RSpec file.

**Step 2:** SSH into node-0 and upload set_up_web_interface.sh.

**Step 3:** Run
'''
chmod +x ./set_up_web_interface.sh.
'''

**Step 4:** Execute ./set_up_web_interface.sh.

**Step 5:** SSH into node-1 and upload set_up_backend.sh.

**Step 6:** Run chmod +x ./set_up_backend.sh.

**Step 7:** Execute ./set_up_backend.sh.

**Step 8:** On note-1, run python3 ./server_base.py
