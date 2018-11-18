library(utils)
library(ggmap)
library(ggplot2)
library(sp)
library(devtools)
library(dplyr)
library(stringr)
library(maps)
library(readxl)
library(Rcpp)
library(tidyverse)
register_google(key='AIzaSyB5r5kI9mTsmsodrc4boJqhejqlPAfNySQ')
UK<-get_map('UK',zoom=5)
RA<-read.csv("C:\\Users\\HP\\Documents\\Maths\\Year 3\\%69%$_ai_hackathon%%1337%%\\road_accident\\Road_Accident\\Road-Accident-data\\Road-Accident.csv")
timestamps<-read_excel("C:\\Users\\HP\\Documents\\Maths\\Year 3\\%69%$_ai_hackathon%%1337%%\\road_accident\\Road_Accident\\Road-Accident-data\\timestamps_next_wave.xlsx")
#The above steps import the dataset and the timestamps. Please load the appropriate files, if they do not immediately load.
timestamps_cleaned<-timestamps
timestamps_cleaned[is.na(timestamps_cleaned)]<-0
road_accident_data=data.frame(RA,timestamps_cleaned)

mapofmaps <- function(k,l,FRAME,COLUMN,LAT,LON, drop=TRUE){
  df<-FRAME
  RA_new <- df[df[, COLUMN, drop=drop] == l,]
  for (i in 0:k){
    if (i==l){
      crash_tot<-nrow(RA_new)
      UK_points<-ggmap(UK)+geom_point(aes(x=RA_new[, LON], y=RA_new[, LAT]), data=RA_new,size=0.001)
      print(crash_tot)
      
    }
  }
  UK_points
}

mapoftime_days <- function(day,k,l,COLUMN,LAT,LON, drop=TRUE){
  start_time<-(1420070700+(day-1)*86400)
  end_time<-(1420070700+(day)*86400)
  df<-subset(road_accident_data,end_time>timestamp &  timestamp>=start_time)
  RA_new <- df[df[, COLUMN, drop=drop] == l,]
  for (i in 0:k){
    if (i==l){
      crash_tot<-nrow(RA_new)
      UK_points<-ggmap(UK)+geom_point(aes(x=RA_new[, LON], y=RA_new[, LAT]), data=RA_new,size=0.001)
      print(crash_tot)
      
    }
  }
  UK_points
}

#Months
Start_Jan<-1420070700
End_Jan<-(1420070700+31*86400)
End_Feb<-(1420070700+59*86400)
End_Mar<-(1420070700+90*86400)
End_Apr<-(1420070700+120*86400)
End_May<-(1420070700+151*86400)
End_Jun<-(1420070700+181*86400)
End_Jul<-(1420070700+212*86400)
End_Aug<-(1420070700+243*86400)
End_Sep<-(1420070700+273*86400)
End_Oct<-(1420070700+304*86400)
End_Nov<-(1420070700+334*86400)
End_Dec<-(1420070700+365*86400)

months<-data.frame(Start_Jan,End_Jan,End_Feb,End_Mar,End_Apr,End_May,End_Jun,End_Jul,End_Aug,End_Sep,End_Oct,End_Nov,End_Dec)

mapoftime_months <- function(month,k,l,COLUMN,LAT,LON, drop=TRUE){
  start_time<-months[[month]]
  end_time<-months[[month+1]]
  df<-subset(road_accident_data,end_time>timestamp &  timestamp>=start_time)
  RA_new <- df[df[, COLUMN, drop=drop] == l,]
  for (i in 0:k){
    if (i==l){
      UK_points<-ggmap(UK)+geom_point(aes(x=RA_new[, LON], y=RA_new[, LAT]), data=RA_new,size=0.001)
      
    }
  }
  UK_points
}

Cas_HM<-ggmap(UK) + stat_density2d(data=RA, mapping=aes(x=longitude, y=latitude, fill=number_of_casualties), geom="polygon", alpha=0.3, fill="red2")+xlab("Longitude")+ylab("Latitude")+ggtitle("Density of Car Crashes \n by No. of Casualties")+ theme(plot.title = element_text(hjust = 0.5))

Age_HM<-ggmap(UK) + stat_density2d(data=RA, mapping=aes(x=longitude, y=latitude, fill=age_band_of_driver), geom="polygon", alpha=0.3, fill="blue2")+xlab("Longitude")+ylab("Latitude")+ggtitle("Density of Car Crashes \n by Age of Driver")+ theme(plot.title = element_text(hjust = 0.5))


