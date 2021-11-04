#include <stdint.h>
#include <pru_cfg.h>
#include "resource_table_empty.h"
#include "prugpio.h"


volatile register unsigned int __R30;
volatile register unsigned int __R31;

void main(void) {
	int i;
	uint32_t *gpio1 = (uint32_t *)GPIO1;
	uint32_t *gpio3 = (uint32_t *)GPIO3;
	
	/* Clear SYSCFG[STANDBY_INIT] to enable OCP master port */
	//	CT_CFG.SYSCFG_bit.STANDBY_INIT = 0;
	
	while(1){
		//gpio1[GPIO_SETDATAOUT]   = USR3;//que the pin to be set high	
		gpio3[GPIO_SETDATAOUT]   = (1 << 14);
		//see if this is compiled away when set to zero
		__delay_cycles(0);//from experiments, this is removed. 
		//gpio1[GPIO_CLEARDATAOUT] = USR3;
		gpio3[GPIO_CLEARDATAOUT] = (1 << 14);//que the pin to be set low
	
		__delay_cycles(0); 

	}
	__halt();
}