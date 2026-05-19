import os
import sys
import subprocess



def run_init_sm_eval(input_dir, output_dir):
    os.chdir(input_dir)
    input_filelist = [os.path.abspath(f) for f in os.listdir()
                      if "model_0." in f]
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.chdir("examples")

    for input_file in input_filelist:
        try:
            _=subprocess.run(["./smorodina_init_score.sh",
                input_file, output_dir], check=True
            )
        except Exception as E:
            print(f"Fail on {input_file}")
            print(e)



if __name__ == "__main__":
    run_init_sm_eval(sys.argv[1], sys.argv[2])