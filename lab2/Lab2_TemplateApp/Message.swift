//
//  Message.swift
//  Lab2_TemplateApp
//
//  Created by k b on 1/18/19.
//  Copyright © 2019 KIS AGH. All rights reserved.
//

import Foundation

class Message {
    var author: String
    var time: Date
    var content: String
    
    init(_author:String, _time: Date, _content: String) {
        self.author = _author
        self.time = _time
        self.content = _content
    }
    
    func getText() -> String {
        return self.content
    }
    
    func getDetails() -> String {
        let byText = NSLocalizedString("by", comment: "")
        let hoursText = NSLocalizedString("hours", comment: "")
        let minutesText = NSLocalizedString("minutes", comment: "")
        let secondsText = NSLocalizedString("seconds", comment: "")
        let agoText = NSLocalizedString("ago", comment: "")
        
        let components = Calendar.current.dateComponents([.hour, .minute, .second], from: self.time, to: Date())
        return byText + " \(self.author), \(components.hour!) \(hoursText), \(components.minute!) \(minutesText) and \(components.second!) \(secondsText) \(agoText)"
    }
}
