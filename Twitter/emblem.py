#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This module is based on the svg_mod by benjamin <benjamin@vidya>
# This is a part of the external Twitter applet for Cairo-Dock
#
# Author: Eduardo Mucelli Rezende Oliveira
# E-mail: edumucelli@gmail.com or eduardom@dcc.ufmg.br

import os

class Emblem:
  def __init__(self):
    self.emblem = os.path.abspath(os.path.join(os.getcwd(), './emblem.svg'))
    self.counter = 0

  def update(self, counter):
    self.counter = counter
    svg = open(self.emblem, 'w')
    svg.write(self.draw())
    svg.close()

  def draw(self):
    emblem_string = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->
<svg xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" version="1.0" width="39.983284" height="39.945618" id="svg2408" inkscape:version="0.48.0 r9654" sodipodi:docname="emblem.svg">
  <sodipodi:namedview pagecolor="#ffffff" bordercolor="#666666" borderopacity="1" objecttolerance="10" gridtolerance="10" guidetolerance="10" inkscape:pageopacity="0" inkscape:pageshadow="2" inkscape:window-width="1280" inkscape:window-height="748" id="namedview94" showgrid="false" inkscape:zoom="3.4546968" inkscape:cx="-27.204217" inkscape:cy="-10.241983" inkscape:window-x="0" inkscape:window-y="0" inkscape:window-maximized="1" inkscape:current-layer="layer4" fit-margin-top="0" fit-margin-left="0" fit-margin-right="0" fit-margin-bottom="0" inkscape:snap-bbox="true" inkscape:snap-page="true"/>
  <defs id="defs2410">
    <linearGradient id="linearGradient3942">
      <stop id="stop3944" style="stop-color:#ffffff;stop-opacity:1" offset="0"/>
      <stop id="stop3946" style="stop-color:#ffffff;stop-opacity:0" offset="1"/>
    </linearGradient>
    <linearGradient id="linearGradient3727">
      <stop id="stop3729" style="stop-color:#d5d5d5;stop-opacity:1" offset="0"/>
      <stop id="stop3731" style="stop-color:#f1f1f1;stop-opacity:1" offset="1"/>
    </linearGradient>
    <linearGradient id="linearGradient3641">
      <stop id="stop3643" style="stop-color:#000000;stop-opacity:1" offset="0"/>
      <stop id="stop3645" style="stop-color:#000000;stop-opacity:0" offset="1"/>
    </linearGradient>
    <linearGradient x1="45.447727" y1="92.539597" x2="45.447727" y2="7.0165396" id="ButtonShadow" gradientUnits="userSpaceOnUse" gradientTransform="scale(1.0058652,0.994169)">
      <stop id="stop3750" style="stop-color:#000000;stop-opacity:1" offset="0"/>
      <stop id="stop3752" style="stop-color:#000000;stop-opacity:0.58823532" offset="1"/>
    </linearGradient>
    <linearGradient id="linearGradient3737">
      <stop id="stop3739" style="stop-color:#ffffff;stop-opacity:1" offset="0"/>
      <stop id="stop3741" style="stop-color:#ffffff;stop-opacity:0" offset="1"/>
    </linearGradient>
    <linearGradient id="linearGradient3700">
      <stop id="stop3702" style="stop-color:#dcdcdc;stop-opacity:1" offset="0"/>
      <stop id="stop3704" style="stop-color:#f0f0f0;stop-opacity:1" offset="1"/>
    </linearGradient>
    <filter color-interpolation-filters="sRGB" id="filter3174">
      <feGaussianBlur id="feGaussianBlur3176" stdDeviation="1.71"/>
    </filter>
    <filter x="-0.192" y="-0.192" width="1.3839999" height="1.3839999" color-interpolation-filters="sRGB" id="filter3794">
      <feGaussianBlur id="feGaussianBlur3796" stdDeviation="5.28"/>
    </filter>
    <linearGradient x1="48" y1="20.220806" x2="48" y2="138.66119" id="linearGradient3613" xlink:href="#linearGradient3737" gradientUnits="userSpaceOnUse"/>
    <radialGradient cx="48" cy="90.171875" r="42" fx="48" fy="90.171875" id="radialGradient3619" xlink:href="#linearGradient3737" gradientUnits="userSpaceOnUse" gradientTransform="matrix(1.1573129,0,0,0.99590774,-7.5510206,0.19713193)"/>
    <clipPath id="clipPath3613">
      <rect width="84" height="84" rx="6" ry="6" x="6" y="6" id="rect3615" style="fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none"/>
    </clipPath>
    <linearGradient x1="48" y1="88" x2="48" y2="32" id="linearGradient3627" xlink:href="#linearGradient3700" gradientUnits="userSpaceOnUse"/>
    <linearGradient x1="48" y1="88" x2="48" y2="36" id="linearGradient3635" xlink:href="#linearGradient3727" gradientUnits="userSpaceOnUse"/>
    <filter color-interpolation-filters="sRGB" id="filter3649">
      <feGaussianBlur id="feGaussianBlur3651" stdDeviation="1.38"/>
    </filter>
    <filter color-interpolation-filters="sRGB" id="filter3665">
      <feGaussianBlur id="feGaussianBlur3667" stdDeviation="0.69"/>
    </filter>
    <linearGradient x1="36.357143" y1="6" x2="36.357143" y2="63.893143" id="linearGradient3687" xlink:href="#linearGradient3737" gradientUnits="userSpaceOnUse"/>
    <linearGradient x1="48" y1="90" x2="48" y2="5.9877172" id="linearGradient3689" xlink:href="#linearGradient3700" gradientUnits="userSpaceOnUse"/>
    <clipPath id="clipPath3696">
      <rect width="84" height="84" rx="6" ry="6" x="106" y="6" id="rect3698" style="fill:#ff00ff;fill-opacity:1;fill-rule:nonzero;stroke:none"/>
    </clipPath>
    <linearGradient x1="48" y1="32" x2="48" y2="80" id="linearGradient3701" xlink:href="#linearGradient3641" gradientUnits="userSpaceOnUse" gradientTransform="translate(100,0)"/>
    <clipPath id="clipPath3703">
      <rect width="84" height="84" rx="6" ry="6" x="106" y="6" id="rect3705" style="fill:#ff00ff;fill-opacity:1;fill-rule:nonzero;stroke:none"/>
    </clipPath>
    <linearGradient x1="51" y1="62" x2="51" y2="21" id="linearGradient3707" xlink:href="#linearGradient3641" gradientUnits="userSpaceOnUse" gradientTransform="translate(100,-1)"/>
    <linearGradient id="linearGradient3737-3">
      <stop id="stop3739-5" style="stop-color:#ffffff;stop-opacity:1" offset="0"/>
      <stop id="stop3741-7" style="stop-color:#ffffff;stop-opacity:0" offset="1"/>
    </linearGradient>
    <radialGradient cx="48" cy="90.171875" r="42" fx="48" fy="90.171875" id="radialGradient2858" xlink:href="#linearGradient3737-3" gradientUnits="userSpaceOnUse" gradientTransform="matrix(1.1573129,0,0,0.99590774,-7.551021,0.1971319)"/>
    <linearGradient x1="45.447727" y1="92.539597" x2="45.447727" y2="7.0165396" id="ButtonShadow-0" gradientUnits="userSpaceOnUse" gradientTransform="matrix(1.0058652,0,0,0.994169,100,0)">
      <stop id="stop3750-8" style="stop-color:#000000;stop-opacity:1" offset="0"/>
      <stop id="stop3752-5" style="stop-color:#000000;stop-opacity:0.58823532" offset="1"/>
    </linearGradient>
    <linearGradient x1="32.251034" y1="6.1317081" x2="32.251034" y2="90.238609" id="linearGradient3780" xlink:href="#ButtonShadow-0" gradientUnits="userSpaceOnUse" gradientTransform="matrix(1.0238095,0,0,1.0119048,-1.1428571,-98.071429)"/>
    <linearGradient x1="32.251034" y1="6.1317081" x2="32.251034" y2="90.238609" id="linearGradient3772" xlink:href="#ButtonShadow-0" gradientUnits="userSpaceOnUse" gradientTransform="matrix(1.0238095,0,0,1.0119048,-1.1428571,-98.071429)"/>
    <linearGradient x1="32.251034" y1="6.1317081" x2="32.251034" y2="90.238609" id="linearGradient3725" xlink:href="#ButtonShadow-0" gradientUnits="userSpaceOnUse" gradientTransform="matrix(1.0238095,0,0,1.0119048,-1.1428571,-98.071429)"/>
    <linearGradient x1="32.251034" y1="6.1317081" x2="32.251034" y2="90.238609" id="linearGradient3721" xlink:href="#ButtonShadow-0" gradientUnits="userSpaceOnUse" gradientTransform="translate(0,-97)"/>
    <linearGradient x1="32.251034" y1="6.1317081" x2="32.251034" y2="90.238609" id="linearGradient2918" xlink:href="#ButtonShadow-0" gradientUnits="userSpaceOnUse" gradientTransform="matrix(1.0238095,0,0,1.0119048,-1.1428571,-98.071429)"/>
    <linearGradient id="linearGradient3801">
      <stop id="stop3803" style="stop-color:#a4d620;stop-opacity:1" offset="0"/>
      <stop id="stop3805" style="stop-color:#62a915;stop-opacity:1" offset="1"/>
    </linearGradient>
    <linearGradient x1="45.298355" y1="72.618279" x2="79.622185" y2="72.618279" id="linearGradient3915" xlink:href="#linearGradient3801" gradientUnits="userSpaceOnUse"/>
    <linearGradient x1="68" y1="52" x2="68" y2="84" id="linearGradient3948" xlink:href="#linearGradient3942" gradientUnits="userSpaceOnUse"/>
    <linearGradient gradientUnits="userSpaceOnUse" xlink:href="#linearGradient3942-7" id="linearGradient3948-1" y2="84" x2="68" y1="52" x1="68"/>
    <linearGradient gradientUnits="userSpaceOnUse" xlink:href="#linearGradient3801-9" id="linearGradient3915-7" y2="72.618279" x2="79.622185" y1="72.618279" x1="45.298355"/>
    <linearGradient id="linearGradient3801-9">
      <stop offset="0" style="stop-color:#a4d620;stop-opacity:1" id="stop3803-1"/>
      <stop offset="1" style="stop-color:#62a915;stop-opacity:1" id="stop3805-7"/>
    </linearGradient>
    <linearGradient gradientTransform="matrix(1.0238095,0,0,1.0119048,-1.1428571,-98.071429)" gradientUnits="userSpaceOnUse" xlink:href="#ButtonShadow-0-0" id="linearGradient2918-0" y2="90.238609" x2="32.251034" y1="6.1317081" x1="32.251034"/>
    <linearGradient gradientTransform="translate(0,-97)" gradientUnits="userSpaceOnUse" xlink:href="#ButtonShadow-0-0" id="linearGradient3721-9" y2="90.238609" x2="32.251034" y1="6.1317081" x1="32.251034"/>
    <linearGradient gradientTransform="matrix(1.0238095,0,0,1.0119048,-1.1428571,-98.071429)" gradientUnits="userSpaceOnUse" xlink:href="#ButtonShadow-0-0" id="linearGradient3725-4" y2="90.238609" x2="32.251034" y1="6.1317081" x1="32.251034"/>
    <linearGradient gradientTransform="matrix(1.0238095,0,0,1.0119048,-1.1428571,-98.071429)" gradientUnits="userSpaceOnUse" xlink:href="#ButtonShadow-0-0" id="linearGradient3772-9" y2="90.238609" x2="32.251034" y1="6.1317081" x1="32.251034"/>
    <linearGradient gradientTransform="matrix(1.0238095,0,0,1.0119048,-1.1428571,-98.071429)" gradientUnits="userSpaceOnUse" xlink:href="#ButtonShadow-0-0" id="linearGradient3780-5" y2="90.238609" x2="32.251034" y1="6.1317081" x1="32.251034"/>
    <linearGradient gradientTransform="matrix(1.0058652,0,0,0.994169,100,0)" gradientUnits="userSpaceOnUse" id="ButtonShadow-0-0" y2="7.0165396" x2="45.447727" y1="92.539597" x1="45.447727">
      <stop offset="0" style="stop-color:#000000;stop-opacity:1" id="stop3750-8-6"/>
      <stop offset="1" style="stop-color:#000000;stop-opacity:0.58823532" id="stop3752-5-1"/>
    </linearGradient>
    <radialGradient gradientTransform="matrix(1.1573129,0,0,0.99590774,-7.551021,0.1971319)" gradientUnits="userSpaceOnUse" xlink:href="#linearGradient3737-3-2" id="radialGradient2858-1" fy="90.171875" fx="48" r="42" cy="90.171875" cx="48"/>
    <linearGradient id="linearGradient3737-3-2">
      <stop offset="0" style="stop-color:#ffffff;stop-opacity:1" id="stop3739-5-2"/>
      <stop offset="1" style="stop-color:#ffffff;stop-opacity:0" id="stop3741-7-6"/>
    </linearGradient>
    <linearGradient gradientTransform="translate(100,-1)" gradientUnits="userSpaceOnUse" xlink:href="#linearGradient3641-7" id="linearGradient3707-7" y2="21" x2="51" y1="62" x1="51"/>
    <clipPath id="clipPath3703-7">
      <rect style="fill:#ff00ff;fill-opacity:1;fill-rule:nonzero;stroke:none" id="rect3705-2" y="6" x="106" ry="6" rx="6" height="84" width="84"/>
    </clipPath>
    <linearGradient gradientTransform="translate(100,0)" gradientUnits="userSpaceOnUse" xlink:href="#linearGradient3641-7" id="linearGradient3701-1" y2="80" x2="48" y1="32" x1="48"/>
    <clipPath id="clipPath3696-8">
      <rect style="fill:#ff00ff;fill-opacity:1;fill-rule:nonzero;stroke:none" id="rect3698-7" y="6" x="106" ry="6" rx="6" height="84" width="84"/>
    </clipPath>
    <linearGradient gradientUnits="userSpaceOnUse" xlink:href="#linearGradient3700-8" id="linearGradient3689-4" y2="5.9877172" x2="48" y1="90" x1="48"/>
    <linearGradient gradientUnits="userSpaceOnUse" xlink:href="#linearGradient3737-8" id="linearGradient3687-0" y2="63.893143" x2="36.357143" y1="6" x1="36.357143"/>
    <filter id="filter3665-9" color-interpolation-filters="sRGB">
      <feGaussianBlur stdDeviation="0.69" id="feGaussianBlur3667-5"/>
    </filter>
    <filter id="filter3649-6" color-interpolation-filters="sRGB">
      <feGaussianBlur stdDeviation="1.38" id="feGaussianBlur3651-4"/>
    </filter>
    <linearGradient gradientUnits="userSpaceOnUse" xlink:href="#linearGradient3727-2" id="linearGradient3635-6" y2="36" x2="48" y1="88" x1="48"/>
    <linearGradient gradientUnits="userSpaceOnUse" xlink:href="#linearGradient3700-8" id="linearGradient3627-2" y2="32" x2="48" y1="88" x1="48"/>
    <clipPath id="clipPath3613-8">
      <rect style="fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none" id="rect3615-9" y="6" x="6" ry="6" rx="6" height="84" width="84"/>
    </clipPath>
    <radialGradient gradientTransform="matrix(1.1573129,0,0,0.99590774,-7.5510206,0.19713193)" gradientUnits="userSpaceOnUse" xlink:href="#linearGradient3737-8" id="radialGradient3619-6" fy="90.171875" fx="48" r="42" cy="90.171875" cx="48"/>
    <linearGradient gradientUnits="userSpaceOnUse" xlink:href="#linearGradient3737-8" id="linearGradient3613-0" y2="138.66119" x2="48" y1="20.220806" x1="48"/>
    <filter id="filter3794-9" color-interpolation-filters="sRGB" height="1.3839999" width="1.3839999" y="-0.192" x="-0.192">
      <feGaussianBlur stdDeviation="5.28" id="feGaussianBlur3796-2"/>
    </filter>
    <filter id="filter3174-1" color-interpolation-filters="sRGB">
      <feGaussianBlur stdDeviation="1.71" id="feGaussianBlur3176-4"/>
    </filter>
    <linearGradient id="linearGradient3700-8">
      <stop offset="0" style="stop-color:#dcdcdc;stop-opacity:1" id="stop3702-4"/>
      <stop offset="1" style="stop-color:#f0f0f0;stop-opacity:1" id="stop3704-3"/>
    </linearGradient>
    <linearGradient id="linearGradient3737-8">
      <stop offset="0" style="stop-color:#ffffff;stop-opacity:1" id="stop3739-6"/>
      <stop offset="1" style="stop-color:#ffffff;stop-opacity:0" id="stop3741-8"/>
    </linearGradient>
    <linearGradient gradientTransform="scale(1.0058652,0.994169)" gradientUnits="userSpaceOnUse" id="ButtonShadow-3" y2="7.0165396" x2="45.447727" y1="92.539597" x1="45.447727">
      <stop offset="0" style="stop-color:#000000;stop-opacity:1" id="stop3750-0"/>
      <stop offset="1" style="stop-color:#000000;stop-opacity:0.58823532" id="stop3752-7"/>
    </linearGradient>
    <linearGradient id="linearGradient3641-7">
      <stop offset="0" style="stop-color:#000000;stop-opacity:1" id="stop3643-4"/>
      <stop offset="1" style="stop-color:#000000;stop-opacity:0" id="stop3645-4"/>
    </linearGradient>
    <linearGradient id="linearGradient3727-2">
      <stop offset="0" style="stop-color:#d5d5d5;stop-opacity:1" id="stop3729-5"/>
      <stop offset="1" style="stop-color:#f1f1f1;stop-opacity:1" id="stop3731-4"/>
    </linearGradient>
    <linearGradient id="linearGradient3942-7">
      <stop offset="0" style="stop-color:#ffffff;stop-opacity:1" id="stop3944-4"/>
      <stop offset="1" style="stop-color:#ffffff;stop-opacity:0" id="stop3946-5"/>
    </linearGradient>
    <linearGradient inkscape:collect="always" xlink:href="#ButtonShadow-3" id="linearGradient3250" gradientUnits="userSpaceOnUse" gradientTransform="scale(1.0058652,0.994169)" x1="45.447727" y1="92.539597" x2="45.447727" y2="7.0165396"/>
    <linearGradient inkscape:collect="always" xlink:href="#linearGradient3801-9" id="linearGradient3252" gradientUnits="userSpaceOnUse" x1="45.298355" y1="72.618279" x2="79.622185" y2="72.618279"/>
    <linearGradient inkscape:collect="always" xlink:href="#linearGradient3942-7" id="linearGradient3254" gradientUnits="userSpaceOnUse" x1="68" y1="52" x2="68" y2="84"/>
  </defs>
  <metadata id="metadata2413">
    <rdf:RDF>
      <cc:Work rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage"/>
        <dc:title/>
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <g id="layer2" style="display:none" transform="translate(-176.03343,-51.028478)">
    <rect width="86" height="85" rx="6" ry="6" x="5" y="7" id="rect3745" style="opacity:0.9;fill:url(#ButtonShadow);fill-opacity:1;fill-rule:nonzero;stroke:none;filter:url(#filter3174)"/>
  </g>
  <g id="layer4" transform="translate(-50.007625,-51.028478)">
    <g id="g3234" transform="matrix(0.68115941,0,0,0.68115941,28.692755,16.26995)">
      <path style="opacity:0.1;color:#000000;fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:2;marker:none;visibility:visible;display:inline;overflow:visible;enable-background:accumulate" id="path3960" inkscape:connector-curvature="0" d="m 89.986349,69.238985 c -0.21488,-1.561093 -1.973583,-1.971086 -3.08095,-2.785965 0.452305,-1.002477 1.307299,-1.880744 1.442147,-2.982622 0.09844,-1.212445 -1.013508,-2.114893 -2.161243,-2.135756 -0.574938,-0.191984 -1.529962,-0.121132 -1.883184,-0.466436 0.105461,-1.303923 0.927598,-2.804937 -0.05258,-3.95302 -0.907896,-1.060888 -2.339545,-0.509432 -3.503632,-0.325674 -0.950635,0.504422 -0.81239,-0.565783 -0.973216,-1.2035 -0.130627,-1.071533 -0.401383,-2.422333 -1.652276,-2.666162 -1.269606,-0.351715 -2.257329,0.785416 -3.345553,1.248885 -0.564682,0.197811 -0.761585,-1.032508 -1.178359,-1.409042 -0.426005,-1.011804 -1.521655,-1.848863 -2.654045,-1.413094 -1.095119,0.436651 -1.63445,1.627605 -2.458205,2.425428 -0.973647,-0.65486 -1.72467,-1.7847 -2.91707,-1.99934 -1.243767,-0.181639 -2.134633,0.905175 -2.372989,2.019516 -0.345055,0.444832 -0.243497,1.842522 -1.003052,1.403006 -1.213096,-0.355405 -2.631658,-1.302577 -3.801916,-0.341572 -1.164288,0.944179 -0.641361,2.603822 -0.785903,3.912444 -1.186176,0.269467 -2.880347,-0.340038 -3.868298,0.741757 -1.026659,1.143887 -0.143349,2.597452 0.237559,3.813095 0.487992,0.76899 -0.891072,0.672735 -1.319748,1.016916 -1.098052,0.268634 -2.195073,1.121664 -2.064313,2.380723 0.249354,1.192288 1.335753,1.97237 1.99934,2.949845 -0.871859,0.915157 -2.269562,1.493314 -2.556533,2.818742 -0.186067,1.142981 0.709312,1.986005 1.663193,2.403037 0.374257,0.418594 1.762649,0.565214 1.196802,1.235928 -0.585967,1.153839 -1.765734,2.450576 -0.926208,3.768425 0.810341,1.207354 2.476744,0.956157 3.736472,1.311043 -0.08576,1.227497 -0.781478,2.521328 -0.229433,3.703695 0.526899,1.071756 1.844115,1.213477 2.87647,0.879241 0.560732,0.07218 1.729076,-0.722239 1.724808,0.155757 0.28962,1.207178 0.140911,2.908592 1.527846,3.422546 1.38487,0.596205 2.576146,-0.697698 3.773565,-1.225564 0.454783,0.276534 0.742145,1.177337 1.132089,1.695641 0.455828,1.285443 2.259105,1.820804 3.255585,0.80819 0.610876,-0.645848 1.17573,-1.360459 1.769908,-2.032116 1.070537,0.696774 1.92142,2.036743 3.310382,1.999339 1.284689,-0.0939 1.81764,-1.335721 2.151522,-2.404812 0.206115,-0.763429 0.45194,-1.441171 1.291319,-0.838121 1.079697,0.400421 2.40691,1.016712 3.407356,0.09643 1.036768,-1.007403 0.54752,-2.574581 0.688297,-3.867575 1.24572,-0.135375 2.670869,0.29881 3.736472,-0.524417 0.936001,-0.804307 0.694064,-2.129136 0.219537,-3.122161 -0.129526,-0.619425 -0.912001,-1.544893 0.15361,-1.604149 1.111548,-0.448238 2.718145,-0.69704 2.904459,-2.123887 0.293747,-1.438242 -1.158981,-2.317711 -1.863365,-3.381883 -0.0012,-0.497479 0.978512,-0.910082 1.354831,-1.374896 0.68176,-0.486375 1.154931,-1.160958 1.098503,-2.027866 z"/>
      <path inkscape:connector-curvature="0" style="opacity:0.15;color:#000000;fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:2;marker:none;visibility:visible;display:inline;overflow:visible;enable-background:accumulate" id="path3956" transform="matrix(0,1.048834,-1.048834,0,146.16452,5.4895435)" d="m 60.9375,54.59375 a 0.86264402,0.86264402 0 0 0 -0.71875,0.4375 L 58.5,57.875 55.625,56.25 a 0.86264402,0.86264402 0 0 0 -1.28125,0.59375 l -0.625,3.3125 -3.28125,-0.5625 a 0.86264402,0.86264402 0 0 0 -1,1 L 50,63.875 46.6875,64.5 a 0.86264402,0.86264402 0 0 0 -0.59375,1.28125 l 1.625,2.875 L 44.875,70.375 A 0.86264402,0.86264402 0 0 0 44.75,71.78125 L 47.25,73.9375 45.15625,76.5 A 0.86264402,0.86264402 0 0 0 45.5,77.875 l 3.15625,1.1875 -1.125,3.15625 a 0.86264402,0.86264402 0 0 0 0.8125,1.15625 l 3.3125,0.03125 0.0625,3.3125 a 0.86264402,0.86264402 0 0 0 1.15625,0.8125 L 56,86.4375 l 1.1875,3.125 a 0.86264402,0.86264402 0 0 0 1.34375,0.34375 l 2.59375,-2.125 2.1875,2.5625 a 0.86264402,0.86264402 0 0 0 1.40625,-0.125 l 1.6875,-2.875 2.9375,1.625 a 0.86264402,0.86264402 0 0 0 1.25,-0.59375 l 0.59375,-3.28125 3.3125,0.5625 a 0.86264402,0.86264402 0 0 0 1,-1 L 74.9375,81.34375 78.21875,80.75 A 0.86264402,0.86264402 0 0 0 78.8125,79.5 l -1.625,-2.9375 2.875,-1.6875 a 0.86264402,0.86264402 0 0 0 0.125,-1.40625 L 77.625,71.28125 79.75,68.6875 a 0.86264402,0.86264402 0 0 0 -0.34375,-1.34375 l -3.125,-1.1875 1.09375,-3.125 A 0.86264402,0.86264402 0 0 0 76.5625,61.875 L 73.25,61.8125 73.21875,58.5 A 0.86264402,0.86264402 0 0 0 72.0625,57.6875 l -3.15625,1.125 -1.1875,-3.15625 a 0.86264402,0.86264402 0 0 0 -1.375,-0.34375 l -2.5625,2.09375 -2.15625,-2.5 a 0.86264402,0.86264402 0 0 0 -0.6875,-0.3125 z"/>
      <path inkscape:connector-curvature="0" style="opacity:0.3;color:#000000;fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:2;marker:none;visibility:visible;display:inline;overflow:visible;enable-background:accumulate" id="path3950" transform="matrix(0,1.048834,-1.048834,0,146.16452,5.4895435)" d="m 74.641931,84.79994 -4.128425,-0.680449 -0.772592,4.112178 -3.646724,-2.051417 -2.132447,3.599941 -2.725174,-3.174954 -3.235096,2.653498 -1.474928,-3.915545 -3.947546,1.387004 -0.04678,-4.183864 -4.183864,-0.04678 1.387005,-3.947547 -3.915546,-1.474927 2.653499,-3.235097 -3.174955,-2.725173 3.599941,-2.132447 -2.051417,-3.646724 4.112178,-0.772592 -0.680448,-4.128426 4.128425,0.680449 0.772592,-4.112178 3.646724,2.051417 2.132447,-3.599941 2.725173,3.174954 3.235097,-2.653498 1.474927,3.915545 3.947547,-1.387004 0.04678,4.183864 4.183863,0.04678 -1.387004,3.947547 3.915545,1.474927 -2.653498,3.235097 3.174955,2.725173 -3.599942,2.132447 2.051418,3.646724 -4.112178,0.772592 z"/>
      <path transform="matrix(0,1.048834,-1.048834,0,146.16452,4.4895435)" inkscape:connector-curvature="0" style="color:#000000;fill:#ff0000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:2;marker:none;visibility:visible;display:inline;overflow:visible;enable-background:accumulate" id="path3139" d="m 74.641931,84.79994 -4.128425,-0.680449 -0.772592,4.112178 -3.646724,-2.051417 -2.132447,3.599941 -2.725174,-3.174954 -3.235096,2.653498 -1.474928,-3.915545 -3.947546,1.387004 -0.04678,-4.183864 -4.183864,-0.04678 1.387005,-3.947547 -3.915546,-1.474927 2.653499,-3.235097 -3.174955,-2.725173 3.599941,-2.132447 -2.051417,-3.646724 4.112178,-0.772592 -0.680448,-4.128426 4.128425,0.680449 0.772592,-4.112178 3.646724,2.051417 2.132447,-3.599941 2.725173,3.174954 3.235097,-2.653498 1.474927,3.915545 3.947547,-1.387004 0.04678,4.183864 4.183863,0.04678 -1.387004,3.947547 3.915545,1.474927 -2.653498,3.235097 3.174955,2.725173 -3.599942,2.132447 2.051418,3.646724 -4.112178,0.772592 z"/>
      <text xml:space="preserve" style="font-size:16px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:-1.32000005px;writing-mode:lr-tb;text-anchor:start;opacity:0.15;fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold" x="59.530632" y="77.325226" id="text3856" sodipodi:linespacing="125%" transform="scale(0.9999961,1.0000039)">
        <tspan sodipodi:role="line" id="tspan3858" x="59.530632" y="77.325226" style="font-size:16px;font-weight:bold;letter-spacing:-1.32000005px;fill:#000000;-inkscape-font-specification:Sans Bold">{0}</tspan>
      </text>
      <path style="opacity:0;fill:#000000;stroke:none;display:inline" id="path3919" inkscape:connector-curvature="0" d="m 60,72 4,-4 4,4 8,-8 4,4 -12,12 -8,-8 z"/>
      <path style="opacity:0.6;color:#000000;fill:url(#linearGradient3948);fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:2;marker:none;visibility:visible;display:inline;overflow:visible;enable-background:accumulate" id="path3933" inkscape:connector-curvature="0" d="M 71.5625,52 68.71875,55.34375 65.3125,52.5625 63.78125,56.65625 59.625,55.1875 l 0,1 4.15625,1.46875 1.53125,-4.09375 3.40625,2.78125 L 71.5625,53 73.8125,56.78125 77.625,54.625 78.4375,58.9375 82.625,58.25 82.78125,57.21875 78.4375,57.9375 77.625,53.625 73.8125,55.78125 71.5625,52 z m -11.96875,7.59375 -4.40625,0.03125 0.34375,1 4.0625,-0.03125 0,-1 z m 22.625,2 -0.15625,0.96875 3.8125,0.71875 0.5,-0.90625 -4.15625,-0.78125 z m -25.875,2.3125 -3.78125,1.40625 0.625,0.78125 3.46875,-1.3125 -0.3125,-0.875 z m 28.3125,2.53125 -0.4375,0.75 3.09375,1.84375 L 88,68.4375 l -3.34375,-2 z M 54.875,69.125 52,71.5625 l 0.6875,0.40625 2.65625,-2.25 L 54.875,69.125 z m 30.25,2.75 -0.46875,0.40625 2.15625,2.625 0.625,-0.21875 -2.3125,-2.8125 z m -29.78125,2.6875 -1.71875,3.0625 0.5,0.09375 1.65625,-2.90625 -0.4375,-0.25 z m 28.3125,2.53125 -0.3125,0.125 1.125,3.15625 0.34375,0 -1.15625,-3.28125 z m -25.875,2.3125 -0.5625,3.375 L 57.375,82.75 57.9375,79.4375 57.78125,79.40625 z"/>
      <text xml:space="preserve" style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;opacity:0.3;fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold" x="60.261475" y="76.597481" id="text3074" sodipodi:linespacing="125%">
        <tspan sodipodi:role="line" id="tspan3076" x="60.261475" y="76.597481" style="font-size:14px;fill:#000000">{0}</tspan>
      </text>
      <text transform="scale(0.9999961,1.0000039)" sodipodi:linespacing="125%" id="text3852" y="78.053253" x="58.71452" style="font-size:18px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:-1.32000005px;writing-mode:lr-tb;text-anchor:start;opacity:0.05;fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold" xml:space="preserve">
        <tspan style="font-size:18px;font-weight:bold;letter-spacing:-2.47000003px;fill:#000000;-inkscape-font-specification:Sans Bold" y="78.053253" x="58.71452" id="tspan3854" sodipodi:role="line">{0}</tspan>
      </text>
      <text sodipodi:linespacing="125%" id="text3070" y="76.097481" x="60.261475" style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;fill:#ff0000;fill-opacity:1;fill-rule:nonzero;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold" xml:space="preserve">
        <tspan style="font-size:14px;fill:#ffffff" y="76.097481" x="60.261475" id="tspan3072" sodipodi:role="line">{0}</tspan>
      </text>
    </g>
  </g>
</svg>"""
    formated_counter = str('%02d' % self.counter)
    return emblem_string.format(formated_counter)     # replaces the '{0}' on the triple-quoted http://stackoverflow.com/questions/3877623/in-python-can-you-have-variables-within-triple-quotes-if-so-how
