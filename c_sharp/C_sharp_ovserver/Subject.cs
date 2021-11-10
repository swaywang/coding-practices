using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace SampleAP
{
    abstract class Subject
    {
        public delegate void StatusUpdate(Subject obj, object arg);
        public event StatusUpdate OnStatusUpdate = null;
        public bool changed = false;

        public void addObserver(Observer o)
        {
            OnStatusUpdate += new StatusUpdate(o.Update);
        }
        
        public void deleteObserver(Observer o)
        {
            OnStatusUpdate -= new StatusUpdate(o.Update);
        }

        public void notifyObservers(Object arg)
        {
            if (OnStatusUpdate != null && changed)
            {
                OnStatusUpdate(this, arg);
            }

            changed = false;
        }

        public void notifyObservers()
        {
            notifyObservers(null);
        }

        public void setChanged()
        {
            changed = true;
        }
    }
}
