# CS-34505

this is a project based on the requirenments from Jira ticket number [34505](https://legacycom.atlassian.net/browse/CS-34505).

in summary, Gannett needs us to update 2 things for 247 sites.

The 2 things are:

* update header/footer URLs for each site
* update header/footer leaderboard ad tags for Desktop and Mobile

action plan on how to tackle this project can be found [here](https://docs.google.com/document/d/1S75a-jkneP3fkny_nUCl_U-UoF5hfGyfO-LR8kxImIE/edit).

### check_heights_and_widths.py

to achieve the requirenments requested in Jira per our action plan ^, we needed to find out if all header/footer `heights` and `widths` were the same.  

they are not. 

to find out, we needed to create a list from inputs received from affiliate to run against our db.  `clear_sitenames()` does that. 

afterwards, ran this agains db:

```
select * 
from dbo.tblaffiliatesettings with (nolock)
where AffiliateSiteName in ('alicetx', 'amarillo', ... ETC
```

and verified that not all `heights` and `widths` are the same.  results [here](https://docs.google.com/spreadsheets/d/1LcJqbe17NXDF89_nc7INKl5UVasKD-SIBH9YNm6utSs/edit#gid=0)

### generate_sql.py

to update header and footer urls for list, the following `sql` script needs to be ran in production:

```
UPDATE dbo.tblaffiliatesettings
SET headerurl = <headerurl>,
	footerurl = <footerurl>,
	artworkdeliveryoption = 3
WHERE affiliatesitename = <sitename>
```

`generate_sql.py` grabs all required data from `csv` file provided by affiliate and creates a copy of the above `sql` script per site. 

resulting sql scrips can be found [here](https://docs.google.com/spreadsheets/d/1LcJqbe17NXDF89_nc7INKl5UVasKD-SIBH9YNm6utSs/edit#gid=263315091)


### generate_hash_table.py

generates the following format, including all 247 cobrands:

```
var gannettHashTable = {
'alicetx': 'tx-alice-mobile-C6683',
};
```

re: trailing commas in the hashtable, _JavaScript has allowed trailing commas in array literals since the beginning, and later added them to object literals (ECMAScript 5) and most recently (ECMAScript 2017) to function parameters._ [1]

---
[1] https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas