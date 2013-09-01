SELECT TOP 100 PERCENT * FROM (
SELECT * FROM (SELECT TOP 100 PERCENT * FROM ( 
SELECT [HOLELOCATION].[HOLEID], 
[HOLELOCATION].[PROJECTCODE], 
[HOLELOCATION].[TENEMENTID], [HOLELOCATION].[GRIDNAME], 
[HOLELOCATION].[HOLETYPE], [HOLELOCATION].[EAST], 
[HOLELOCATION].[NORTH], [HOLELOCATION].[RL], 
[HOLELOCATION].[DEPTH], [HOLELOCATION].[PROSPECT], 
[HOLELOCATION].[STARTDATE], [HOLELOCATION].[ENDDATE], 
[HOLEDETAILS].[Grid_Original], 
[HOLEDETAILS].[Logged_By], [HOLECOMMENT].[DrillCompany], 
[HOLEDETAILS].[Rig], [HOLECOORD].[AMG_Z50_X], 
[HOLECOORD].[AMG_Z50_Y], [HOLECOORD].[AMG_Z50_Z], 
[HOLECOORD].[Merlot_X], [HOLECOORD].[Merlot_Y], 
[HOLECOORD].[Merlot_Z], [HOLECOORD].[MGA_Z50_X], 
[HOLECOORD].[MGA_Z50_Y], [HOLECOORD].[MGA_Z50_Z], 
[HOLECOORD].[WGS84_X], [HOLECOORD].[WGS84_Y], 
[HOLECOORD].[WGS84_Z], [HOLECOORD].[South_X], 
[HOLECOORD].[South_Y], [HOLECOORD].[South_Z], 
[HOLECOORD].[Mine_X], [HOLECOORD].[Mine_Y], 
[HOLECOORD].[Mine_Z], [HOLECOORD].[Uground_X], 
[HOLECOORD].[Uground_Y], [HOLECOORD].[Uground_Z], 
[HOLECOMMENT].[Status], [HOLECOMMENT].[HoleComments] FROM HOLELOCATION INNER JOIN (
SELECT * FROM [HOLELOCATION]) AS [CollarWSF] ON [CollarWSF].[HOLEID] = [HOLELOCATION].[HOLEID] AND [CollarWSF].[PROJECTCODE] = [HOLELOCATION].[PROJECTCODE] LEFT JOIN (SELECT [HOLEDETAILS].[HOLEID], 
[HOLEDETAILS].[PROJECTCODE], min(CASE when [HOLEDETAILS].[NAME] = 'Grid_Original' then [HOLEDETAILS].[VALUE] ELSE NULL END) as [Grid_Original], 
min(CASE when [HOLEDETAILS].[NAME] = 'Logged_By' then [HOLEDETAILS].[VALUE] ELSE NULL END) as [Logged_By], 
min(CASE when [HOLEDETAILS].[NAME] = 'Rig' then [HOLEDETAILS].[VALUE] ELSE NULL END) as [Rig] FROM [HOLEDETAILS] WHERE [HOLEDETAILS].[NAME] IN ('Grid_Original', 
'Logged_By', 'Rig') GROUP BY [HOLEDETAILS].[PROJECTCODE], 
[HOLEDETAILS].[HOLEID])[HOLEDETAILS] ON [HOLELOCATION].[PROJECTCODE] = [HOLEDETAILS].[PROJECTCODE] AND [HOLELOCATION].[HOLEID] = [HOLEDETAILS].[HOLEID] LEFT JOIN (SELECT [HOLECOMMENT].[HOLEID], 
[HOLECOMMENT].[PROJECTCODE], min(CASE when [HOLECOMMENT].[NAME] = 'DrillCompany' then [HOLECOMMENT].[VALUE] ELSE NULL END) as [DrillCompany], 
min(CASE when [HOLECOMMENT].[NAME] = 'Status' then [HOLECOMMENT].[VALUE] ELSE NULL END) as [Status], 
min(CASE when [HOLECOMMENT].[NAME] = 'HoleComments' then [HOLECOMMENT].[VALUE] ELSE NULL END) as [HoleComments] FROM [HOLECOMMENT] WHERE [HOLECOMMENT].[NAME] IN ('DrillCompany', 
'Status', 'HoleComments') GROUP BY [HOLECOMMENT].[PROJECTCODE], 
[HOLECOMMENT].[HOLEID])[HOLECOMMENT] ON [HOLELOCATION].[PROJECTCODE] = [HOLECOMMENT].[PROJECTCODE] AND [HOLELOCATION].[HOLEID] = [HOLECOMMENT].[HOLEID] LEFT JOIN (SELECT [HOLECOORD].[HOLEID], 
[HOLECOORD].[PROJECTCODE], min(CASE when [HOLECOORD].[COORDINATESET] = 'AMG_Z50' then [HOLECOORD].[X] ELSE NULL END) as [AMG_Z50_X], 
min(CASE when [HOLECOORD].[COORDINATESET] = 'AMG_Z50' then [HOLECOORD].[Y] ELSE NULL END) as [AMG_Z50_Y], 
min(CASE when [HOLECOORD].[COORDINATESET] = 'AMG_Z50' then [HOLECOORD].[Z] ELSE NULL END) as [AMG_Z50_Z], 
min(CASE when [HOLECOORD].[COORDINATESET] = 'Merlot' then [HOLECOORD].[X] ELSE NULL END) as [Merlot_X], 
min(CASE when [HOLECOORD].[COORDINATESET] = 'Merlot' then [HOLECOORD].[Y] ELSE NULL END) as [Merlot_Y], 
min(CASE when [HOLECOORD].[COORDINATESET] = 'Merlot' then [HOLECOORD].[Z] ELSE NULL END) as [Merlot_Z], 
min(CASE when [HOLECOORD].[COORDINATESET] = 'MGA_Z50' then [HOLECOORD].[X] ELSE NULL END) as [MGA_Z50_X], 
min(CASE when [HOLECOORD].[COORDINATESET] = 'MGA_Z50' then [HOLECOORD].[Y] ELSE NULL END) as [MGA_Z50_Y], 
min(CASE when [HOLECOORD].[COORDINATESET] = 'MGA_Z50' then [HOLECOORD].[Z] ELSE NULL END) as [MGA_Z50_Z], 
min(CASE when [HOLECOORD].[COORDINATESET] = 'WGS84' then [HOLECOORD].[X] ELSE NULL END) as [WGS84_X], 
min(CASE when [HOLECOORD].[COORDINATESET] = 'WGS84' then [HOLECOORD].[Y] ELSE NULL END) as [WGS84_Y], 
min(CASE when [HOLECOORD].[COORDINATESET] = 'WGS84' then [HOLECOORD].[Z] ELSE NULL END) as [WGS84_Z], 
min(CASE when [HOLECOORD].[COORDINATESET] = 'South' then [HOLECOORD].[X] ELSE NULL END) as [South_X], 
min(CASE when [HOLECOORD].[COORDINATESET] = 'South' then [HOLECOORD].[Y] ELSE NULL END) as [South_Y], 
min(CASE when [HOLECOORD].[COORDINATESET] = 'South' then [HOLECOORD].[Z] ELSE NULL END) as [South_Z], 
min(CASE when [HOLECOORD].[COORDINATESET] = 'Mine' then [HOLECOORD].[X] ELSE NULL END) as [Mine_X], 
min(CASE when [HOLECOORD].[COORDINATESET] = 'Mine' then [HOLECOORD].[Y] ELSE NULL END) as [Mine_Y], 
min(CASE when [HOLECOORD].[COORDINATESET] = 'Mine' then [HOLECOORD].[Z] ELSE NULL END) as [Mine_Z], 
min(CASE when [HOLECOORD].[COORDINATESET] = 'Uground' then [HOLECOORD].[X] ELSE NULL END) as [Uground_X], 
min(CASE when [HOLECOORD].[COORDINATESET] = 'Uground' then [HOLECOORD].[Y] ELSE NULL END) as [Uground_Y], 
min(CASE when [HOLECOORD].[COORDINATESET] = 'Uground' then [HOLECOORD].[Z] ELSE NULL END) as [Uground_Z] FROM [HOLECOORD] GROUP BY [HOLECOORD].[PROJECTCODE], 
[HOLECOORD].[HOLEID])[HOLECOORD] ON [HOLELOCATION].[PROJECTCODE] = [HOLECOORD].[PROJECTCODE] AND [HOLELOCATION].[HOLEID] = [HOLECOORD].[HOLEID]) [ACQTMP]  ) AS [TMPVIEW7]) AS [TMPVIEW99]  WHERE (([TMPVIEW99].[PROJECTCODE] = 'Merlot') AND ([TMPVIEW99].[HOLEID] IN ('SRC122', 
'SRC123', 'RPN123', 'RPN124'))) ORDER BY [TMPVIEW99].[PROJECTCODE] ASC, [TMPVIEW99].[HOLEID] ASC