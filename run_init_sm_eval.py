import os
import sys
import subprocess



def run_init_sm_eval(input_dir, output_dir, pmpnn_dir):
    os.chdir(input_dir)
    input_filelist = [os.path.abspath(f) for f in os.listdir()]
    os.chdir(pmpnn_dir)

    for input_file in input_filelist:
        try:
            _=subprocess.run(["./examples/smorodina_init_score.sh",
                input_file, output_dir], check=True
            )
        except Exception as E:
            print(f"Fail on {input_file}")
            print(e)



if __name__ == "__main__":
    run_init_sm_eval(sys.argv[1], sys.argv[2])