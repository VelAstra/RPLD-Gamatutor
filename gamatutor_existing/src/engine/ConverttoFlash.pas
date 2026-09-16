unit ConverttoFlash;

interface

uses Windows, SysUtils, Classes, Graphics, Forms, Controls, StdCtrls,
  Buttons, ExtCtrls,primitif,Dialogs, MPlayer,desainer;

type
  TFlash = class(TForm)
    Image1: TImage;
    PaintBox1: TPaintBox;
    zoomTimer1: TTimer;
    zoomTimer2: TTimer;
    SaveDialog1: TSaveDialog;

    procedure PaintBox1Click(Sender: TObject);
    procedure FormShow(Sender: TObject);
    procedure zoomTimer1Timer(Sender: TObject);
    procedure zoomTimer2Timer(Sender: TObject);
    procedure FormClose(Sender: TObject; var Action: TCloseAction);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Flash: TFlash;

implementation
uses shellAPI, PointerMouse,preview;

var
  ErrorOrExitCode : cardinal;

{$R *.dfm}

function ExecuteAndWait(AFilename : String; AParameter : string;
                        ACmdShow : Integer; var AErrorOrExitCode : Cardinal): Boolean;
var
  StartupInfo: TStartupInfo;
  ProcessInfo: TProcessInformation;
  S : String;
begin
  FillChar(StartupInfo,Sizeof(StartupInfo),0);
  StartupInfo.cb := Sizeof(StartupInfo);
  StartupInfo.dwFlags := STARTF_USESHOWWINDOW;
  StartupInfo.wShowWindow := ACmdShow;
  S := AParameter;
  UniqueString(S);
  if not CreateProcess(PChar(AFilename),PChar(S),nil,nil,False,
                       CREATE_NEW_CONSOLE or NORMAL_PRIORITY_CLASS,nil,nil,
                       StartupInfo,ProcessInfo) then
    begin
      Result := False;
      AErrorOrExitCode := GetLastError;
    end
  else
    begin
      Result := True;
      WaitforSingleObject(ProcessInfo.hProcess,INFINITE);
      GetExitCodeProcess(ProcessInfo.hProcess,AErrorOrExitCode);
      CloseHandle(ProcessInfo.hProcess);
      CloseHandle(ProcessInfo.hThread);
    end;
end;

procedure TFlash.PaintBox1Click(Sender: TObject);
begin
   {flash.Close;
   timer1.Enabled:=false;
   ShellExecute(Self.Handle,nil,pchar(extractfilepath(paramstr(0))+'script\Stop Camstudio.exe'), nil, nil, SW_SHOWMINIMIZED);
   setresolution(PrevX,PrevY);  }
end;

procedure TFlash.FormShow(Sender: TObject);
var
  item,sounditem:listofimage;

begin

 {*************inisialisasi untuk sound***************}
 filepath:= mainform.Edit1.Text;
 filesound:= mainform.Edit2.Text;
 {******************update May 23, 2008***************}
 mediaplayer1pos :=0;

 {************************update on March 17, 2009********************}
 try
  //if(form1.speedbutton1.Enabled=true)then
  //begin
    if (listframe.Count>0) then
    begin
      //bolehzooming:=true;
      new(item);
      item:=listframe.Items[prevanimcount];

      if((prevanimcount>=listframe.Count-1)and(prevanimcursor>=item.ImagePointer.Count-1)) then
         //or(form1.trackbar1.Position>=form1.trackbar1.Max))then
      begin
        //form1.richedit1.Lines.Clear;
        AnimCount:=0;
        counter:=0;
        prevanimcount:=0;
        prevanimcursor:=0;
        //form1.trackbar1.Position:=0;
      end;

      {***************play audio - Update on March 18, 2009**************************}
      new(sounditem);
      sounditem:=listframe.Items[0];
      if (sounditem.ImageSound.Count > 0) then
      begin
        form2.mediaplayer1.FileName:= sounditem.ImageSound.Strings[0] + sounditem.ImageSound.Strings[1];
        if (mediaplayer1pos = 0) then
        begin
          form2.mediaplayer1.Open;
        end;
        //mediaplayer1.Play;
        zoomtimer2.Enabled:=true;
      end;
  {***************************************************}
      animstatus:=true;

      {update 1 Des 2015 camstudio diganti ffmpeg}
      //ShellExecute(Self.Handle,nil,pchar(extractfilepath(paramstr(0))+'script\Open Camstudio.exe'), nil, nil, SW_SHOWMINIMIZED);

      //ShellExecute(Self.Handle,nil,'cmd.exe','/K c:\gamatutor\ffmpeg.exe -f gdigrab -framerate 10 -i desktop  gamatutor.flv',nil, SW_SHOWMINIMIZED);
      //ShellExecute(Self.Handle,nil,'cmd.exe','/K c:\gamatutor\ffmpeg.exe -f gdigrab -i title=TutorialGenerator  gamatutor.flv',nil, SW_SHOWMINIMIZED);

      ShowWindow(FindWindow('Shell_TrayWnd', nil), SW_HIDE);
      ShellExecute(Self.Handle,nil,'cmd.exe','/K c:\gamatutor\ffmpeg.exe -y -f gdigrab -show_region 1 -draw_mouse 0 -i desktop -video_size 800x600 -offset_x 0 -offset_y 0 gamatutor.mkv',nil, SW_HIDE);
      //ShellExecute(Self.Handle,nil,'cmd.exe','/K c:\gamatutor\ffmpeg.exe -y -f gdigrab -show_region 1 -draw_mouse 0 -i desktop gamatutor.mkv',nil, SW_HIDE);


      zoomtimer1.Enabled:=true;
    end;
  //end;
 except
 end;
end;

procedure TFlash.zoomTimer1Timer(Sender: TObject);
var
  previtem,animateitem:listofimage;
  animcursor,prevpointer:listofpointer;
  temp:listofimage;
  temppoint:Tpoint;

  //StartInfo: TStartupInfo;
  //ProcInfo: TProcessInformation;


begin


   {*********************************update on March 17, 2009*****************************************}
   try
   prevAnimCount:=animcount;
   prevAnimCursor:=counter;

   if ((listframe<>nil)and(listframe.Count > 0))then
   begin
     new(animateitem);
     animateitem:=listframe.Items[animcount];
     {*****************************************************************}
     if ((counter=0)and(animateitem.ImageText.Count>0)) then
        //and (fileexists(extractfilepath(paramstr(0))+'ImageText.rtf')))then
     begin
       sleep(300);
       //animateitem.ImageText.SaveToFile(extractfilepath(paramstr(0))+'ImageText.rtf');
       //Richedit1.Lines.LoadFromFile(extractfilepath(paramstr(0))+'ImageText.rtf');
     end;
     {*****************************************************************}
     if((animcount=0)and(animateitem<>nil))then
     begin
       new(animcursor);
       if(animateitem.ImagePointer.Count=1)then
       begin
         animcursor:=animateitem.ImagePointer.Items[counter];
         temppoint.X:=(animcursor.RectSize.Left+animcursor.RectSize.Right) div 2;
         temppoint.Y:=(animcursor.RectSize.Top+animcursor.RectSize.Bottom) div 2;
         previewku.InitCursor(temp,animateitem.ImageFile,animcursor.PointerFile,animcursor.RectSize,temppoint,'0');
         //if(bolehzooming=false)then
         //begin
         //  previewku.AnimationExecute(invalRect,invalcur,true,rect1,rect2,paintbox1,paintbox2,image1,temp,animateitem,0,counter);
         //end else
         {************************************************************}
         //if(bolehzooming=true)then
         //begin
           previewku.ZoomAnimationExecute(invalRect,invalcur,true,flash.PaintBox1,flash.image1,temp,animateitem,0,counter);
         //end;
         {************************************************************}
         if(animateitem<>listframe.Last)then
         begin
           new(nextitem);
           nextitem:=listframe.Items[animcount+1];
           if(nextitem<>nil)then
           begin
             if ((animcursor.PointerSecondPos.X<>-999)
                and(animcursor.PointerSecondPos.Y<>-999))then
             begin
               {if(bolehzooming=false)then
               begin
                  previewku.AnimationExecute(invalrect,invalcur,true,rect1,rect2,paintbox1,paintbox2,image1,animateitem,nextItem,counter,counter);
               end else
               {************************************************************}
               {if(bolehzooming=true)then
               begin }
                 previewku.ZoomAnimationExecute(invalRect,invalcur,true,flash.PaintBox1,flash.image1,animateitem,nextItem,counter,counter);
               //end;
               {************************************************************}
             end else
             begin
               {if(bolehzooming=false)then
               begin
                 previewku.AnimationExecute(invalrect,invalcur,false,rect1,rect2,paintbox1,paintbox2,image1,animateitem,nextItem,counter,counter);
               end else
               {************************************************************}
               {if(bolehzooming=true)then
               begin  }
                 previewku.ZoomAnimationExecute(invalRect,invalcur,false,flash.PaintBox1,flash.image1,animateitem,nextItem,counter,counter);
               //end;
               {************************************************************}
             end;
             counter:=0;
             animcount:=animcount+1;

           end;
         end else
         begin
           {update 1 Des 2015 camstudio diganti ffmpeg}
           //ShellExecute(Self.Handle,nil,pchar(extractfilepath(paramstr(0))+'script\Stop Camstudio.exe'), nil, nil, SW_SHOWMINIMIZED);
           //ShellExecute(Self.Handle,nil,pchar(extractfilepath(paramstr(0))+'ffmpeg\stop_ffmpeg.bat'), nil, nil, SW_SHOWMINIMIZED);
           ShowWindow(FindWindow('Shell_TrayWnd', nil), SW_SHOW);
           //ShellExecute(Self.Handle,nil,'cmd.exe','/K c:\gamatutor\ffmpeg.exe -y -i gamatutor.mkv -c:v copy -c:a copy -pix_fmt yuv420p -preset slow -movflags faststart gamatutor.mp4',nil, SW_HIDE);

           //ShellExecute(Self.Handle,nil,'cmd.exe','/K c:\gamatutor\ffmpeg.exe -y -i gamatutor.mkv -c:v copy -c:a copy -movflags faststart gamatutor.mp4',nil, SW_HIDE);

           ShellExecute(Self.Handle,nil,'cmd.exe','/K c:\gamatutor\ffmpeg.exe -y -i gamatutor.mkv -c:v libx264 -profile:v baseline -c:a libfaac -movflags faststart -pix_fmt yuv420p gamatutor.mp4',nil, SW_HIDE);



           zoomtimer1.Enabled:=false;
           zoomtimer2.Enabled:=false;


           if savedialog1.Execute = true then
           begin

             renamefile('gamatutor.mp4',savedialog1.FileName);

            //renamefile('gamatutor.mp4',FFileName);
            ShellExecute(Self.Handle,nil,'cmd.exe','/C taskkill /im ffmpeg.exe /t /f',nil, SW_HIDE);
           end;


           setresolution(PrevX,PrevY);
           mediaplayer1pos :=0;
           counter:=0;
           animcount:=0;
           flash.Close;


         end;
         {***********************************************************************}
       end else
       if(animateitem.ImagePointer.Count>1)then
       begin
         animcursor:=animateitem.ImagePointer.Items[counter];
         if(animcursor=animateitem.ImagePointer.First)then
         begin
           temppoint.X:=(animcursor.RectSize.Left+animcursor.RectSize.Right) div 2;
           temppoint.Y:=(animcursor.RectSize.Top+animcursor.RectSize.Bottom) div 2;
           previewku.InitCursor(temp,animateitem.ImageFile,animcursor.PointerFile,animcursor.RectSize,temppoint,'0');
           {if(bolehzooming=false)then
           begin
             previewku.AnimationExecute(invalrect,invalcur,true,rect1,rect2,paintbox1,paintbox2,image1,temp,animateitem,0,counter);
           end else
           {************************************************************}
           {if(bolehzooming=true)then
           begin }
             previewku.ZoomAnimationExecute(invalRect,invalcur,true,flash.PaintBox1,flash.image1,temp,animateitem,0,counter);
           //end;
           {************************************************************}
           counter:=counter+1;

         end else
         if(animcursor=animateitem.ImagePointer.Last)then
         begin
           if(animateitem<>listframe.Last)then
           begin
             new(nextitem);
             nextitem:=listframe.Items[animcount+1];
             if(nextitem<>nil)then
             begin
               if ((animcursor.PointerSecondPos.X<>-999)
                  and(animcursor.PointerSecondPos.Y<>-999))then
               begin
                 {if(bolehzooming=false)then
                 begin
                   previewku.AnimationExecute(invalrect,invalcur,true,rect1,rect2,paintbox1,paintbox2,image1,animateitem,animateitem,counter-1,counter);
                 end else
                 {************************************************************}
                 {if(bolehzooming=true)then
                 begin }
                   previewku.ZoomAnimationExecute(invalRect,invalcur,true,flash.PaintBox1,flash.image1,animateitem,animateitem,counter-1,counter);
                 //end;
                 {************************************************************}
                 {if(bolehzooming=false)then
                 begin
                   previewku.AnimationExecute(invalrect,invalcur,true,rect1,rect2,paintbox1,paintbox2,image1,animateitem,nextItem,counter,counter);
                 end else
                 {************************************************************}
                 {if(bolehzooming=true)then
                 begin  }
                   previewku.ZoomAnimationExecute(invalRect,invalcur,true,flash.PaintBox1,flash.image1,animateitem,nextItem,counter,counter);
                 //end;
                 {************************************************************}
               end else
               begin
                 {if(bolehzooming=false)then
                 begin
                   previewku.AnimationExecute(invalrect,invalcur,true,rect1,rect2,paintbox1,paintbox2,image1,animateitem,nextItem,counter-1,counter);
                 end else
                 {************************************************************}
                 {if(bolehzooming=true)then
                 begin  }
                   previewku.ZoomAnimationExecute(invalRect,invalcur,true,flash.PaintBox1,flash.image1,animateitem,nextItem,counter-1,counter);
                 //end;
                 {************************************************************}
               end;
               counter:=0;
               animcount:=animcount+1;

             end;
           end else
           begin
             {if(bolehzooming=false)then
             begin
               previewku.AnimationExecute(invalrect,invalcur,true,rect1,rect2,paintbox1,paintbox2,image1,animateitem,animateitem,counter-1,counter);
             end else
             {************************************************************}
             {if(bolehzooming=true)then
             begin }
               previewku.ZoomAnimationExecute(invalRect,invalcur,true,flash.PaintBox1,flash.image1,animateitem,animateitem,counter-1,counter);
             //end;
             {************************************************************}
             {update 1 Des 2015 camstudio diganti ffmpeg}
             //ShellExecute(Self.Handle,nil,pchar(extractfilepath(paramstr(0))+'script\Stop Camstudio.exe'), nil, nil, SW_SHOWMINIMIZED);
             //ShellExecute(Self.Handle,nil,pchar(extractfilepath(paramstr(0))+'ffmpeg\stop_ffmpeg.bat'), nil, nil, SW_SHOWMINIMIZED);
             ShowWindow(FindWindow('Shell_TrayWnd', nil), SW_SHOW);


             //ShellExecute(Self.Handle,nil,'cmd.exe','/K c:\gamatutor\ffmpeg.exe -y -i gamatutor.mkv -c:v copy -c:a copy -movflags faststart gamatutor.mp4',nil, SW_HIDE);
             ShellExecute(Self.Handle,nil,'cmd.exe','/K c:\gamatutor\ffmpeg.exe -y -i gamatutor.mkv -c:v libx264 -profile:v baseline -c:a libfaac -movflags faststart -pix_fmt yuv420p gamatutor.mp4',nil, SW_HIDE);


             zoomtimer1.Enabled:=false;
             zoomtimer2.Enabled:=false;



           
           if savedialog1.Execute = true then
           begin

             renamefile('gamatutor.mp4',savedialog1.FileName);
            //renamefile('gamatutor.mp4',FFileName);
            ShellExecute(Self.Handle,nil,'cmd.exe','/C taskkill /im ffmpeg.exe /t /f',nil, SW_HIDE);
           end;


             setresolution(PrevX,PrevY);

             mediaplayer1pos :=0;
             counter:=0;
             animcount:=0;
             flash.Close;



           end;
         end else
         begin
           {if(bolehzooming=false)then
           begin
             previewku.AnimationExecute(invalrect,invalcur,true,rect1,rect2,paintbox1,paintbox2,image1,animateitem,animateitem,counter-1,counter);
           end else
           {************************************************************}
           {if(bolehzooming=true)then
           begin   }
             previewku.ZoomAnimationExecute(invalRect,invalcur,true,flash.PaintBox1,flash.image1,animateitem,animateitem,counter-1,counter);
           //end;
           {************************************************************}
           counter:=counter+1;

         end;
       end else
       begin

         {update 1 Des 2015 camstudio diganti ffmpeg}
         //ShellExecute(Self.Handle,nil,pchar(extractfilepath(paramstr(0))+'script\Stop Camstudio.exe'), nil, nil, SW_SHOWMINIMIZED);
         //ShellExecute(Self.Handle,nil,pchar(extractfilepath(paramstr(0))+'ffmpeg\stop_ffmpeg.bat'), nil, nil, SW_SHOWMINIMIZED);
         ShowWindow(FindWindow('Shell_TrayWnd', nil), SW_SHOW);
         //ShellExecute(Self.Handle,nil,'cmd.exe','/K c:\gamatutor\ffmpeg.exe -y -i gamatutor.mkv -c:v copy -c:a copy -movflags faststart gamatutor.mp4',nil, SW_HIDE);
         ShellExecute(Self.Handle,nil,'cmd.exe','/K c:\gamatutor\ffmpeg.exe -y -i gamatutor.mkv -c:v libx264 -profile:v baseline -c:a libfaac -movflags faststart -pix_fmt yuv420p gamatutor.mp4',nil, SW_HIDE);


         zoomtimer1.Enabled:=false;
         zoomtimer2.Enabled:=false;
        
            
           if savedialog1.Execute = true then
           begin

             renamefile('gamatutor.mp4',savedialog1.FileName);
            //renamefile('gamatutor.mp4',FFileName);
            ShellExecute(Self.Handle,nil,'cmd.exe','/C taskkill /im ffmpeg.exe /t /f',nil, SW_HIDE);
           end;



         setresolution(PrevX,PrevY);

         mediaplayer1pos :=0;
         counter:=0;
         animcount:=0;
         flash.Close;


       end;
     end else
     if((animcount>0)and(animateitem<>nil))then
     begin
       new(animcursor);
       if(animateitem.ImagePointer.Count=1)then
       begin
         animcursor:=animateitem.ImagePointer.Items[counter];
         new(previtem);
         previtem:=listframe.Items[animcount-1];
         new(prevpointer);
         prevpointer:=previtem.ImagePointer.Last;

         if ((prevpointer.PointerSecondPos.X<>-999)
            and(prevpointer.PointerSecondPos.Y<>-999))then
         begin
           previewku.InitCursor(temp,animateitem.ImageFile,prevpointer.PointerFile,prevpointer.RectSize,prevpointer.PointerSecondPos,animateitem.ImageName);
         end else
         begin
           previewku.InitCursor(temp,animateitem.ImageFile,prevpointer.PointerFile,prevpointer.RectSize,prevpointer.PointerFirstPos,animateitem.ImageName);
         end;
         {if(bolehzooming=false)then
         begin
           previewku.AnimationExecute(invalrect,invalcur,true,rect1,rect2,paintbox1,paintbox2,image1,temp,animateitem,0,counter);
         end else
         {************************************************************}
         {if(bolehzooming=true)then
         begin   }
           previewku.ZoomAnimationExecute(invalRect,invalcur,true,flash.PaintBox1,flash.image1,temp,animateitem,0,counter);
         //end;
         {************************************************************}

         if(animateitem<>listframe.Last)then
         begin
           new(nextitem);
           nextitem:=listframe.Items[animcount+1];
           if(nextitem<>nil)then
           begin
             if ((animcursor.PointerSecondPos.X<>-999)
                and(animcursor.PointerSecondPos.Y<>-999))then
             begin
               {if(bolehzooming=false)then
               begin
                 previewku.AnimationExecute(invalrect,invalcur,true,rect1,rect2,paintbox1,paintbox2,image1,animateitem,nextItem,counter,counter);
               end else
               {************************************************************}
               {if(bolehzooming=true)then
               begin }
                 previewku.ZoomAnimationExecute(invalRect,invalcur,true,flash.PaintBox1,flash.image1,animateitem,nextItem,counter,counter);
               //end;
               {************************************************************}
             end else
             begin
               {if(bolehzooming=false)then
               begin
                 previewku.AnimationExecute(invalrect,invalcur,false,rect1,rect2,paintbox1,paintbox2,image1,animateitem,nextItem,counter,counter);
               end else
               {************************************************************}
               {if(bolehzooming=true)then
               begin }
                 previewku.ZoomAnimationExecute(invalRect,invalcur,false,flash.PaintBox1,flash.image1,animateitem,nextItem,counter,counter);
               //end;
               {************************************************************}
             end;
             counter:=0;
             animcount:=animcount+1;

           end;
         end else
         begin
           {update 1 Des 2015 camstudio diganti ffmpeg}
           //ShellExecute(Self.Handle,nil,pchar(extractfilepath(paramstr(0))+'script\Stop Camstudio.exe'), nil, nil, SW_SHOWMINIMIZED);
           //ShellExecute(Self.Handle,nil,pchar(extractfilepath(paramstr(0))+'ffmpeg\stop_ffmpeg.bat'), nil, nil, SW_SHOWMINIMIZED);
           ShowWindow(FindWindow('Shell_TrayWnd', nil), SW_SHOW);
           //ShellExecute(Self.Handle,nil,'cmd.exe','/K c:\gamatutor\ffmpeg.exe -y -i gamatutor.mkv -c:v copy -c:a copy -movflags faststart gamatutor.mp4',nil, SW_HIDE);
           ShellExecute(Self.Handle,nil,'cmd.exe','/K c:\gamatutor\ffmpeg.exe -y -i gamatutor.mkv -c:v libx264 -profile:v baseline -c:a libfaac -movflags faststart -pix_fmt yuv420p gamatutor.mp4',nil, SW_HIDE);


           zoomtimer1.Enabled:=false;
           zoomtimer2.Enabled:=false;
           
            
           if savedialog1.Execute = true then
           begin

             renamefile('gamatutor.mp4',savedialog1.FileName);
            //renamefile('gamatutor.mp4',FFileName);
            ShellExecute(Self.Handle,nil,'cmd.exe','/C taskkill /im ffmpeg.exe /t /f',nil, SW_HIDE);
           end;


           setresolution(PrevX,PrevY);

           mediaplayer1pos :=0;
           counter:=0;
           animcount:=0;
           flash.Close;


         end;
         {***********************************************************************}
       end else
       if(animateitem.ImagePointer.Count>1)then
       begin
         animcursor:=animateitem.ImagePointer.Items[counter];
         if(animcursor=animateitem.ImagePointer.First)then
         begin
           new(previtem);
           previtem:=listframe.Items[animcount-1];
           new(prevpointer);
           prevpointer:=previtem.ImagePointer.Last;

           if ((prevpointer.PointerSecondPos.X<>-999)
            and(prevpointer.PointerSecondPos.Y<>-999))then
           begin
             previewku.InitCursor(temp,animateitem.ImageFile,prevpointer.PointerFile,prevpointer.RectSize,prevpointer.PointerSecondPos,animateitem.ImageName);
           end else
           begin
             previewku.InitCursor(temp,animateitem.ImageFile,prevpointer.PointerFile,prevpointer.RectSize,prevpointer.PointerFirstPos,animateitem.ImageName);
           end;
           {if(bolehzooming=false)then
           begin
             previewku.AnimationExecute(invalrect,invalcur,true,rect1,rect2,paintbox1,paintbox2,image1,temp,animateitem,0,counter);
           end else
           {************************************************************}
           {if(bolehzooming=true)then
           begin }
              previewku.ZoomAnimationExecute(invalRect,invalcur,true,flash.PaintBox1,flash.image1,temp,animateitem,0,counter);
           //end;
           {************************************************************}

           counter:=counter+1;

         end else
         if(animcursor=animateitem.ImagePointer.Last)then
         begin
           if(animateitem<>listframe.Last)then
           begin
             new(nextitem);
             nextitem:=listframe.Items[animcount+1];
             if(nextitem<>nil)then
             begin
               if ((animcursor.PointerSecondPos.X<>-999)
                  and(animcursor.PointerSecondPos.Y<>-999))then
               begin
                 {if(bolehzooming=false)then
                 begin
                   previewku.AnimationExecute(invalrect,invalcur,true,rect1,rect2,paintbox1,paintbox2,image1,animateitem,animateitem,counter-1,counter);
                 end else
                 {************************************************************}
                 {if(bolehzooming=true)then
                 begin  }
                   previewku.ZoomAnimationExecute(invalRect,invalcur,true,flash.PaintBox1,flash.image1,animateitem,animateitem,counter-1,counter);
                 //end;
                 {************************************************************}
                 {if(bolehzooming=false)then
                 begin
                   previewku.AnimationExecute(invalrect,invalcur,true,rect1,rect2,paintbox1,paintbox2,image1,animateitem,nextItem,counter,counter);
                 end else
                 {************************************************************}
                 {if(bolehzooming=true)then
                 begin  }
                   previewku.ZoomAnimationExecute(invalRect,invalcur,true,flash.PaintBox1,flash.image1,animateitem,nextItem,counter,counter);
                 //end;
                 {************************************************************}
               end else
               begin
                 {if(bolehzooming=false)then
                 begin
                   previewku.AnimationExecute(invalrect,invalcur,true,rect1,rect2,paintbox1,paintbox2,image1,animateitem,nextItem,counter-1,counter);
                 end else
                 {************************************************************}
                 {if(bolehzooming=true)then
                 begin    }
                   previewku.ZoomAnimationExecute(invalRect,invalcur,true,flash.PaintBox1,flash.image1,animateitem,nextItem,counter-1,counter);
                 //end;
                 {************************************************************}
               end;
               counter:=0;
               animcount:=animcount+1;

             end;
           end else
           begin
             {if(bolehzooming=false)then
             begin
               previewku.AnimationExecute(invalrect,invalcur,true,rect1,rect2,paintbox1,paintbox2,image1,animateitem,animateitem,counter-1,counter);
             end else
             {************************************************************}
             {if(bolehzooming=true)then
             begin }
               previewku.ZoomAnimationExecute(invalRect,invalcur,true,flash.PaintBox1,flash.image1,animateitem,animateitem,counter-1,counter);
             //end;
             {************************************************************}
             {update 1 Des 2015 camstudio diganti ffmpeg}
             //ShellExecute(Self.Handle,nil,pchar(extractfilepath(paramstr(0))+'script\Stop Camstudio.exe'), nil, nil, SW_SHOWMINIMIZED);
             //ShellExecute(Self.Handle,nil,pchar(extractfilepath(paramstr(0))+'ffmpeg\stop_ffmpeg.bat'), nil, nil, SW_SHOWMINIMIZED);
             ShowWindow(FindWindow('Shell_TrayWnd', nil), SW_SHOW);
             //ShellExecute(Self.Handle,nil,'cmd.exe','/K c:\gamatutor\ffmpeg.exe -y -i gamatutor.mkv -c:v copy -c:a copy -movflags faststart gamatutor.mp4',nil, SW_HIDE);
             ShellExecute(Self.Handle,nil,'cmd.exe','/K c:\gamatutor\ffmpeg.exe -y -i gamatutor.mkv -c:v libx264 -profile:v baseline -c:a libfaac -movflags faststart -pix_fmt yuv420p gamatutor.mp4',nil, SW_HIDE);


             zoomtimer1.Enabled:=false;
             zoomtimer2.Enabled:=false;
             

           if savedialog1.Execute = true then
           begin

             renamefile('gamatutor.mp4',savedialog1.FileName);
            //renamefile('gamatutor.mp4',FFileName);
            ShellExecute(Self.Handle,nil,'cmd.exe','/C taskkill /im ffmpeg.exe /t /f',nil, SW_HIDE);
           end;

             setresolution(PrevX,PrevY);

             mediaplayer1pos :=0;
             counter:=0;
             animcount:=0;
             flash.Close;



           end;
         end else
         begin
           {if(bolehzooming=false)then
           begin
             previewku.AnimationExecute(invalrect,invalcur,true,rect1,rect2,paintbox1,paintbox2,image1,animateitem,animateitem,counter-1,counter);
           end else
           {************************************************************}
           {if(bolehzooming=true)then
           begin }
             previewku.ZoomAnimationExecute(invalRect,invalcur,true,flash.PaintBox1,flash.image1,animateitem,animateitem,counter-1,counter);
           //end;
           {************************************************************}
           counter:=counter+1;

         end;
       end else
       begin
         {update 1 Des 2015 camstudio diganti ffmpeg}
         //ShellExecute(Self.Handle,nil,pchar(extractfilepath(paramstr(0))+'script\Stop Camstudio.exe'), nil, nil, SW_SHOWMINIMIZED);
         //ShellExecute(Self.Handle,nil,pchar(extractfilepath(paramstr(0))+'ffmpeg\stop_ffmpeg.bat'), nil, nil, SW_SHOWMINIMIZED);
         ShowWindow(FindWindow('Shell_TrayWnd', nil), SW_SHOW);
         //ShellExecute(Self.Handle,nil,'cmd.exe','/K c:\gamatutor\ffmpeg.exe -y -i gamatutor.mkv -c:v copy -c:a copy -movflags faststart gamatutor.mp4',nil, SW_HIDE);
         ShellExecute(Self.Handle,nil,'cmd.exe','/K c:\gamatutor\ffmpeg.exe -y -i gamatutor.mkv -c:v libx264 -profile:v baseline -c:a libfaac -movflags faststart -pix_fmt yuv420p gamatutor.mp4',nil, SW_HIDE);


         zoomtimer1.Enabled:=false;
         zoomtimer2.Enabled:=false;
         
             
           if savedialog1.Execute = true then
           begin

             renamefile('gamatutor.mp4',savedialog1.FileName);
            //renamefile('gamatutor.mp4',FFileName);
            ShellExecute(Self.Handle,nil,'cmd.exe','/C taskkill /im ffmpeg.exe /t /f',nil, SW_HIDE);
           end;


         setresolution(PrevX,PrevY);

         mediaplayer1pos :=0;
         counter:=0;
         animcount:=0;
         flash.Close;


       end;
     end else
     begin
       {update 1 Des 2015 camstudio diganti ffmpeg}
       //ShellExecute(Self.Handle,nil,pchar(extractfilepath(paramstr(0))+'script\Stop Camstudio.exe'), nil, nil, SW_SHOWMINIMIZED);
       //ShellExecute(Self.Handle,nil,pchar(extractfilepath(paramstr(0))+'ffmpeg\stop_ffmpeg.bat'), nil, nil, SW_SHOWMINIMIZED);
       ShowWindow(FindWindow('Shell_TrayWnd', nil), SW_SHOW);
       //ShellExecute(Self.Handle,nil,'cmd.exe','/K c:\gamatutor\ffmpeg.exe -y -i gamatutor.mkv -c:v copy -c:a copy -movflags faststart gamatutor.mp4',nil, SW_HIDE);
       ShellExecute(Self.Handle,nil,'cmd.exe','/K c:\gamatutor\ffmpeg.exe -y -i gamatutor.mkv -c:v libx264 -profile:v baseline -c:a libfaac -movflags faststart -pix_fmt yuv420p gamatutor.mp4',nil, SW_HIDE);


       zoomtimer1.Enabled:=false;
       zoomtimer2.Enabled:=false;

       
           if savedialog1.Execute = true then
           begin

             renamefile('gamatutor.mp4',savedialog1.FileName);
            //renamefile('gamatutor.mp4',FFileName);
            ShellExecute(Self.Handle,nil,'cmd.exe','/C taskkill /im ffmpeg.exe /t /f',nil, SW_HIDE);
           end;


       setresolution(PrevX,PrevY);
       mediaplayer1pos :=0;
       counter:=0;
       animcount:=0;
       flash.Close;


     end;
   end else
   begin
     {update 1 Des 2015 camstudio diganti ffmpeg}
     //ShellExecute(Self.Handle,nil,pchar(extractfilepath(paramstr(0))+'script\Stop Camstudio.exe'), nil, nil, SW_SHOWMINIMIZED);
     //ShellExecute(Self.Handle,nil,pchar(extractfilepath(paramstr(0))+'ffmpeg\stop_ffmpeg.bat'), nil, nil, SW_SHOWMINIMIZED);
     ShowWindow(FindWindow('Shell_TrayWnd', nil), SW_SHOW);
     //ShellExecute(Self.Handle,nil,'cmd.exe','/K c:\gamatutor\ffmpeg.exe -y -i gamatutor.mkv -c:v copy -c:a copy -movflags faststart gamatutor.mp4',nil, SW_HIDE);
     ShellExecute(Self.Handle,nil,'cmd.exe','/K c:\gamatutor\ffmpeg.exe -y -i gamatutor.mkv -c:v libx264 -profile:v baseline -c:a libfaac -movflags faststart -pix_fmt yuv420p gamatutor.mp4',nil, SW_HIDE);


     zoomtimer1.Enabled:=false;
     zoomtimer2.Enabled:=false;


            
           if savedialog1.Execute = true then
           begin

             renamefile('gamatutor.mp4',savedialog1.FileName);
            //renamefile('gamatutor.mp4',FFileName);
            ShellExecute(Self.Handle,nil,'cmd.exe','/C taskkill /im ffmpeg.exe /t /f',nil, SW_HIDE);
           end;


     setresolution(PrevX,PrevY);
     mediaplayer1pos :=0;
     counter:=0;
     animcount:=0;
     flash.Close;


   end;

   {***************************************}
   //trackbar1.Position:=trackbar1.Position+1;
   {***************************************}
 //  trackbar1.Position:=previewku.SearchPosition(posarray,prevanimcount,prevanimcursor);
 //  checkallownextPrev(prevanimcount,prevanimcursor,listframe);
 except
   showmessage('Your Scenario is not valid');
   application.Terminate;
 end;
end;

procedure TFlash.zoomTimer2Timer(Sender: TObject);
begin

  form2.mediaplayer1.Play;
  mediaplayer1pos :=form2.mediaplayer1.Position;

end;

procedure TFlash.FormClose(Sender: TObject; var Action: TCloseAction);
var
  sounditem : listofimage;
begin


  if (listframe.Count > 0) then
   begin
     new(sounditem);
     sounditem:=listframe.Items[0];
     if ((sounditem.ImageSound.Count = 0) and (filepath <> '')and (filesound<>''))then
     begin
       sounditem.ImageSound.Add(filepath);
       sounditem.ImageSound.Add(filesound);
     end;
   end;
   {***************untuk stop audio************************}
   if (form2.mediaplayer1.Mode = mpOpen) or (form2.mediaplayer1.Mode = mpPlaying) then
   begin
     form2.mediaplayer1.Position:=0;
     mediaplayer1pos := form2.mediaplayer1.Position;
     zoomtimer2.Enabled:=false;
   end;

    //trackbar1.Position:=0;
    prevanimcount:=0;
    prevanimcursor:=0;
    animcount:=0;
    counter:=0;
    image1.Picture:=nil;
    //image2.Picture:=nil;
    zoomtimer1.Enabled:=false;
    //timer2.Enabled:=false;
    mainform.Edit1.Text:= filepath;
    mainform.Edit2.Text:=filesound;

    deletefile('gamatutor.mkv');

end;

end.

