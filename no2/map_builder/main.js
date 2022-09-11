const height_max = 50;
const width_max = 50;

let date_btn = new Array(height_max);

let chosen_value = 2;

function make_grid ()
{
    for(let i= 0; i< height_max;i++)
    {
        date_btn[i] = new Array(width_max);
    }

    for(let y = 0; y<height_max; y++)
    {
        make_row(y);
        for(let x = 0; x<width_max; x++)
        {
            date_btn[y][x] = 1;
            append_row(y,x);
        }
    }
    return;
}
function make_row(count)
{
    let list_new  = document.createElement("ul");
    list_new.classList.add(`list-${count}`)
    let main_list = document.getElementById("main_list");
    main_list.appendChild(document.createElement("br"));
    main_list.appendChild(list_new);
}
function append_row(row_,colum_)
{
    let main_list = document.getElementsByClassName(`list-${row_}`)[0];
    let list_btn = document.createElement("li");
    let btn_new = document.createElement("button");
    btn_new.classList.add("std_button");
    btn_new.setAttribute("id",`${row_};${colum_}`)
    btn_new.setAttribute("onclick","change(this.id)")
    list_btn.appendChild(btn_new);
    main_list.appendChild(list_btn);
}

function change(id_new)
{
    let row_now = id_new.split(";")[0];
    let colum_now = id_new.split(";")[1];
    if(date_btn[row_now][colum_now] != chosen_value)
    {
        document.getElementById(id_new).style["background-color"] = color_switch(chosen_value,true);
        date_btn[row_now][colum_now] = chosen_value;
    }
    console.log(date_btn);
}

function change_state(id_in)
{
    chosen_value = parseInt(id_in[3]);
    document.getElementById("color_chosen_show").style["background-color"] = color_switch(chosen_value,false);
}

function color_switch(color_value, change_)
{
    switch(color_value)
        {
            case 1:
                return "#000";
                break;
            case 2:
                return "#fff";
                break;
            case 3:
                return "#00f";
                break;
            case 4:
                return "#0f0";
                break;
            case 5:
                return "#f00";
                break;
            case 6:
                return "#0ff";
                break;
            case 7:
                if(change_ == true)
                {
                    player_pos_set()
                }
                return "#f0f";
                break;
            case 8:
                return "#dad";
                break;
        }
}

/*
TODO
-change state --> show  --> done
-clear  --> done
-build  --> 
-player begin --> done
*/

function player_pos_set()
{
    for(let y = 0; y<height_max; y++)
    {
        for(let x = 0; x<width_max; x++)
        {
            if(date_btn[x][y] == 7)
            {
                date_btn[x][y] = 1;
                document.getElementById(`${x};${y}`).style["background-color"] = "#000";    
            }
        }
    }
}

function reset()
{
    for(let y = 0; y<height_max; y++)
    {
        for(let x = 0; x<width_max; x++)
        {
            document.getElementById(`${x};${y}`).style["background-color"] = "#000";
            date_btn[y][x] = 1;
        }
    }
}

function exporting()
{
    let output = "";
    for(let y = 0; y<height_max; y++)
    {
        output += "[";
        for(let x = 0; x<width_max; x++)
        {
            output  += `\"${date_btn[x][y]}\",`;
        }
        output = output.substring(0, output.length - 1);
        output += "],";
        output += "\n";
    }
    output = output.substring(0, output.length - 1);
    output = output.substring(0, output.length - 1);
    copyStringToClipboard(output);
    alert("added to clipboard");
}

function copyStringToClipboard (str) {
    // Temporäres Element erzeugen
    var el = document.createElement('textarea');
    // Den zu kopierenden String dem Element zuweisen
    el.value = str;
    // Element nicht editierbar setzen und aus dem Fenster schieben
    el.setAttribute('readonly', '');
    el.style = {position: 'absolute', left: '-9999px'};
    document.body.appendChild(el);
    // Text innerhalb des Elements auswählen
    el.select();
    // Ausgewählten Text in die Zwischenablage kopieren
    document.execCommand('copy');
    // Temporäres Element löschen
    document.body.removeChild(el);
}