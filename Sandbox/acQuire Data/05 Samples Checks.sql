SELECT TOP 100 PERCENT * FROM (
SELECT * FROM (SELECT TOP 100 PERCENT * FROM (
SELECT [QV_SAMPLE_CHECK].[SAMPLEID] AS [SAMPLEID], 
[QV_SAMPLE_CHECK].[DUPLICATENO] AS [DUPLICATENO], 
[QV_SAMPLE_CHECK].[HOLEID] AS [HOLEID], 
[QV_SAMPLE_CHECK].[PROJECTCODE] AS [PROJECTCODE], 
[QV_SAMPLE_CHECK].[POINTPROSPECT] AS [POINTPROSPECT], 
[QV_SAMPLE_CHECK].[POINTGRIDNAME] AS [POINTGRIDNAME], 
[QV_SAMPLE_CHECK].[POINTTENEMENTID] AS [POINTTENEMENTID], [QV_SAMPLE_CHECK].[SAMP
FROM] AS [SAMPFROM], [QV_SAMPLE_CHECK].[SAMPTO] AS [SAMPTO], 
[QV_SAMPLE_CHECK].[SAMPLETYPE] AS [SAMPLETYPE], 
[QV_SAMPLE_CHECK].[POINTEAST] AS [POINTEAST], 
[QV_SAMPLE_CHECK].[POINTNORTH] AS [POINTNORTH], 
[QV_SAMPLE_CHECK].[POINTRL] AS [POINTRL], 
[QV_SAMPLE_CHECK].[PRIORITY] AS [PRIORITY], 
[QV_SAMPLE_CHECK].[STANDARDID] AS [STANDARDID], 
[QV_SAMPLE_CHECK].[PSAMPLEID] AS [PSAMPLEID], 
[QV_SAMPLE_CHECK].[PDUPLICATENO] AS [PDUPLICATENO], 
[QV_SAMPLE_CHECK].[CHECKSTAGE] AS [CHECKSTAGE], 
[QV_SAMPLE_CHECK].[FRACTIONID] AS [FRACTIONID] 
FROM [QV_SAMPLE_CHECK]) [ACQTMP]) [TMPVIEW11]) AS [TMPVIEW99]  
WHERE (([TMPVIEW99].[HOLEID] IN ('SRC122', 'SRC123', 'RPN123', 'RPN124')))