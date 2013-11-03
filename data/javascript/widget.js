/*
 * THIS VERSION IS FOR USE ON FSF.ORG ONLY - SSL FIXES! 
 *
 * widget.js -- Fundraising web widget
 * Copyright (c) 2007 Creative Commons
 * Copyright (c) 2007 Free Software Foundation, Inc.
 *
 * Modified by the FSF in November 2007 to make it FSF-specific.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 *
 * A copy of the GNU Lesser General Public License is available at
 * <http://www.gnu.org/licenses/lgpl-3.0.html>.
 */

if (fsf_widget_text == "Help protect your freedom!") {
    var fsf_widget_text = "Help protect your freedom!";
	}

if (fsf_widget_text == "Help fight DRM!") {
    var fsf_widget_text = "Help protect your freedom!";
	}



document.write("<link href=\"/graphics/widget/progress.css\" rel=\"stylesheet\" type=\"text/css\" />");
document.write("<link href=\"/graphics/widget/campaignwidget.css?1.0.1\" rel=\"stylesheet\" type=\"text/css\" />");
document.write("");
document.write("<div id=\"fsf_campaign_widget\" class=\"" + fsf_widget_size + "\">");
document.write("<div id=\"fsf_campaign_widget_bg\"><div id=\"fsf_campaign_widget_bg_logo\">");
document.write("<h1 id=\"fsf_widget_title\"><span><a href=\"http://www.fsf.org\">Free Software Foundation</a></span></h1>");
document.write("<p id=\"fsf_widget_text\"><a href=\"https://www.fsf.org/associate/support_freedom/join_fsf\">" + fsf_widget_text + "</a></p>");
document.write("<div id=\"campaign\">");
document.write("<div class=\"progress\" >");
document.write("<span>&nbsp;</span>");
document.write("</div>");
document.write("<div class=\"results\"> &nbsp;&nbsp;463 / 500 new members</div>");
document.write("</div>");
document.write("<div id=\"donors\">");
document.write("<strong>Supporters</strong><br/>");
document.write("<a href=\"http://FIXME/\">529 have contributed</a>");
document.write("</div>");
document.write("");
document.write("<form method=\"get\" action=\"https://www.fsf.org/associate/support_freedom/join_fsf\">");
document.write("");
document.write("<input name=\"referrer\" value='" + fsf_associate_id + "' type=\"hidden\" />");
document.write("");
document.write("&nbsp;<input type=\"submit\" id=\"fsf_widget_donation_btn\" value=\"Join the FSF\" />");
document.write("");
document.write("</form>");
document.write("");
document.write("</div></div>");
document.write("</div>");
document.write("");
