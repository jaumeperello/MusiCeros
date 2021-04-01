import sys
from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
import os
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def ytdl_check():
    path = os.getcwd()
    reqs = subprocess.check_output(['pip', 'list', '-o'])
    # logging.info(reqs.decode('ascii'))
    if "youtube-dl" in reqs.decode('ascii'):
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-U', 'youtube-dl'])
        reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'install', '-U', 'youtube-dl'])
        logging.info(reqs.decode('ascii'))
        bashCommand = f"{path}/run.sh stop"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        logging.info(output.decode('ascii'))
        bashCommand = f"{path}/run.sh start"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        logging.info(output.decode('ascii'))


def main():
    ytdl_check()
    scheduler = BlockingScheduler()
    scheduler.add_job(ytdl_check, 'interval', hours=1)
    logging.info("Started")
    scheduler.start()
    logging.info("Ended")


if __name__ == "__main__":
    main()
