Class dc.Gdown Extends %CSP.Page
{

ClassMethod OnPreHTTP() As %Boolean [ ServerOnly = 1 ]
{
  #dim %response as %CSP.Response
  set %rcc=$Get(%request.Data("GBL",1),"")
  if %rcc]"" {
    set %rcd=$D(@("^"_%rcc))
    if %rcd {
      set %response.ContentType="application/xml"
      set %response.Headers("Content-Disposition")="attachment; filename="""_%rcc_".xml"""
    }
  }
  else  { 
    set %rcd=0
    set %rcc="Parameter GBL"
  }  
  quit $$$OK
}

ClassMethod OnPage() As %Status
{
  if '%rcd {
  &html<<html><head></head><body>
   #(%rcc)# &gt;&gt; not found </body></html>>
  quit $$$OK
  }
  do $system.OBJ.Export(%rcc_".GBL")
  Quit $$$OK
}
}
