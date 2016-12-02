/* Leap year is True if year (modulo 400 || 100 || 4) is true */

#include <stdio.h>

typedef struct
{
	char *m_name;
	int n_days, l_days; //n_days stands for normal and l_days stands for leap days. MAYBE l_days will be deprecated!
}	s_months;

void generate_months(s_months months[])
{
	/* January */ 		months[0].n_days = 31;	months[0].m_name = "January";
	/* February */ 	months[1].n_days = 29;	months[1].m_name = "February";	//We need to stop to 28 so we assume that february hai 29 max days
	/* March */ 		months[2].n_days = 31;	months[2].m_name = "March";
	/* April */ 		months[3].n_days = 30;	months[3].m_name = "April";
	/* May */ 			months[4].n_days = 31;	months[4].m_name = "May";
	/* June */ 			months[5].n_days = 30;	months[5].m_name = "June";
	/* July */ 			months[6].n_days = 31;	months[6].m_name = "July";
	/* August */ 		months[7].n_days = 31;	months[7].m_name = "August";
	/* Sptember */ 	months[8].n_days = 30;	months[8].m_name = "Sptember";
	/* October */ 		months[9].n_days = 31;	months[9].m_name = "October";
	/* November */ 	months[10].n_days = 30;	months[10].m_name = "November";
	/* December */ 	months[11].n_days = 31;	months[11].m_name = "December";
}

int is_leap(int x)
{
	if (x % 4 || x % 100 || x % 400) return 1;
	else return 0;
}

int main()
{
	char day[][10] = { "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" };
	s_months months[12]; generate_months(months);
	int month, year, m_day, wn_day = 3, i, is_sunday = 0; //m_day = month day number & wn_day = number corresponding to week name day of the current month;
	
	for (year = 1901; year <= 2000; year++)
	{
		for (month = 0; month <= 11; month++)	//for each month
		{
			printf("\n\n%i -> %s\n", year, months[month].m_name);
			//printf("M\tT\tW\tT\tF\tS\tS\n\n");
			//for (i = 0; i <= (7 - wn_day)%7; i++) printf("\t"); //Adjust space to print each day below each week_day_name
			
			if (is_leap(year))	//we count all February days (29);
				for (m_day = 1; m_day <= months[month].n_days; m_day++)	//print each day
				{	
					if (m_day==1 && wn_day == 0) is_sunday++;
					if (!((m_day+1) % 7)) printf("\n");
					wn_day = ((wn_day+1) % 7);	
					printf ("%i->%s ", m_day, day[wn_day]);
				}
			else	//We stop February when we reach day 28th;
				for (m_day = 1; m_day <= months[month].n_days; m_day++)	//print each day
				{	
					if (!(month == 2 && m_day == 28))
					{
						if (m_day==1 && wn_day == 0) is_sunday++;
						if (!((m_day+1) % 7)) printf("\n");
						wn_day = ((wn_day+1) % 7);	
						printf ("%i->%s ", m_day, day[wn_day]);
					}
				}
		}
	}

printf("\nSyndays number: %i\n", is_sunday);
return 0;
}








