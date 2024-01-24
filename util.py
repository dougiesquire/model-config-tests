import time
import subprocess as sp

def wait_for_qsub(run_id):
    """
    Wait for the qsub job to terminate.
    """

    while True:
        #time.sleep(10*60)
        time.sleep(1*60)
        try:
            qsub_out = sp.check_output(['qstat', run_id], stderr=sp.STDOUT)
        except sp.CalledProcessError as err:
            qsub_out = err.output

        qsub_out = qsub_out.decode()

        if 'Job has finished' in qsub_out:
            break
