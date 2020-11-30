#include "iec61850_server.h"
#include "hal_thread.h"
#include <signal.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <time.h>


#include "static_model.h"

/* import IEC 61850 device model created from SCL-File */
extern IedModel iedModel;
static int running = 0;

static void
connectionHandler (IedServer self, ClientConnection connection, bool connected, void* parameter)
{
    if (connected)
        printf("Connection opened\n");
	// Else print 'connection closed'
	else
        printf("Connection closed\n");
	// END TASK 1.
}

int main(int argc, char** argv) {

    int tcpPort = 102;

    if (argc > 1) {
        tcpPort = atoi(argv[1]);
    }


	IedServer myServer = IedServer_create(&iedModel);

	IedServer_setConnectionIndicationHandler(myServer, (IedConnectionIndicationHandler) connectionHandler, NULL);

	IedServer_start(myServer, tcpPort);
	if (!IedServer_isRunning(myServer)) {
		printf("Starting server failed! Exit.\n");
		IedServer_destroy(myServer);
		exit(-1);
	}

	running = 1;
        while(running){
		IedServer_lockDataModel(myServer);
		IedServer_unlockDataModel(myServer);
        Thread_sleep(1000);  //update time (milliseconds) from the file


    //** To read .csv file and display
        int rows, cols;
        float value[1][1];  //values of "rows" and "columns" in .csv file
        FILE * fPtr =fopen("randomnumber.csv", "r");

            for(rows=0; rows<1; rows++){
                for(cols=0; cols<1; cols++){
                    fscanf(fPtr, "%f\n", &value[rows][cols]);
                    printf("Value: %.2f \n", value[rows][cols]); //printing the values in the terminal
                }
            printf("\n");
    }
        fclose(fPtr);


		float voltage2 = value[0][0];
		MmsValue* voltageValue2 = MmsValue_newFloat(voltage2);
		IedServer_updateAttributeValue(myServer,IEDMODEL_Device1_MMXU2_PhV_mag_f,voltageValue2);


	}

	IedServer_stop(myServer); //stop MMS server - close TCP server socket and all client sockets
	IedServer_destroy(myServer); // Cleanup - free all resources

}
