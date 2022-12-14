FUNCTION Read_Runlog_File, runlogFilename, OLD=old

record = { col1: '', $
           runlab: '', $
           iyr: 0L, $
           iset:0L, $
           zpdtim: 0.0D, $
           oblat: 0.0D, $
           oblon: 0.0D, $
           zobs: 0.0D, $
           asza: 0.0D, $
           zenoff: 0.0D, $
           opd: 0.0D, $
           fovi: 0.0D, $
           fovo: 0.0D, $
           amal: 0.0D, $
           ifirst: 0L, $
           ilast: 0L, $
           graw: 0.0D, $
           possp: 0L, $
           bytepw: 0L, $
           zoff: 0.0D, $
           snr: 0.0D, $
           apf: '', $
           tins: 0.0D, $
           pins: 0.0D, $
           hins: 0.0D, $
           tout: 0.0D, $
           pout: 0.0D, $
           hout: 0.0D, $
           lasf: 0.0D, $
           wavtkr: 0.0D, $
           sia: 0.0D, $
           sis: 0.0D, $
           aipl: 0.0D, $
           spec_id: 0LL $
         }

   oldFormat = '(a1,a21,1x,2i4,f8.4,f8.3,f9.3,2f8.3,f7.0,f7.2,3f6.0,2i8,f15.11,i8,i3,1x,2f5.0,1x,a2,2(f6.0,f8.0,f5.0),f10.0,f7.0,2f6.1,f7.3,i18)'

   newFormat = '(a1,a35,1x,2i4,f8.4,f8.3,f9.3,2f8.3,1x,f6.4,f7.2,3f6.0,2i8,1x,f14.11,i8,i3,1x,f5.3,i5,1x,a2,2(f6.1,f8.2,f5.1),f10.3,f7.0,2f6.1,f7.3,i18)'

   recordChunkSize = 500

   OpenR, lun, runlogFilename, /GET_LUN, ERROR=openErr
   IF (openErr NE 0) THEN Message, !Error_State.msg, /NONAME

   headerStr=''
   ReadF, lun, headerStr

   ;PrintF, newLun, headerStr

   runlogInfo = replicate(record, recordChunkSize)

   lineCount = 0
   WHILE (eof(lun) NE 1) DO BEGIN
       IF Keyword_Set(old) THEN BEGIN
           ReadF, lun, record, FORMAT=oldFormat
       ENDIF ELSE BEGIN
           ReadF, lun, record, FORMAT=newFormat 
       ENDELSE

       if (lineCount gt n_elements(runlogInfo)-1) then begin
           print, 'Rebuilding to: ', n_elements(runlogInfo) + recordChunkSize
           newRunlogInfo = replicate(record, n_elements(runlogInfo) + recordChunkSize)
           newRunlogInfo[0:lineCount-1] = runlogInfo[0:lineCount-1]
           runlogInfo = newRunlogInfo
       endif

       runlogInfo[lineCount] = record
       lineCount = lineCount + 1

   ENDWHILE

   Free_Lun, lun

   runlogInfo = runlogInfo[0:lineCount-1]

   return, runlogInfo

END
