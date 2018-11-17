package com.example.bb.picassoapp;

import android.content.Context;
import android.os.Environment;
import android.os.Handler;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.ImageView;

import com.squareup.picasso.Callback;
import com.squareup.picasso.MemoryPolicy;
import com.squareup.picasso.NetworkPolicy;
import com.squareup.picasso.Picasso;

import java.io.File;
import java.util.logging.Level;
import java.util.logging.Logger;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        final int option = 13;

        final String url = "https://www.dike.lib.ia.us/images/sample-1.jpg/image";
        final String url2 = "http://drupalsn.com/files/projects/screenshots/sample.jpg";

        // enable picasso logging
        Picasso.with(getApplicationContext()).setLoggingEnabled(true);

        // get app context
        final Context ctx = getApplicationContext();

        // get activity items
        final ImageView img = (ImageView) findViewById(R.id.img);

        // draw images

        // 4. simple image load from internet
        if (option == 4) {
            Picasso
                    .with(ctx)
                    .load(url)
                    .into(img);
        }

        // 5. simple image load from drawable
        if (option == 5) {
            Picasso.with(ctx).load(R.drawable.img).into(img);
        }

        // 6. cache
        if (option == 6) {
            MemoryPolicy[] memoryPolicies = { MemoryPolicy.NO_CACHE, MemoryPolicy.NO_STORE };
            MemoryPolicy memoryPolicy = memoryPolicies[0];

            NetworkPolicy[] networkPolicies = { NetworkPolicy.NO_CACHE, NetworkPolicy.NO_STORE, NetworkPolicy.OFFLINE };
            NetworkPolicy networkPolicy = networkPolicies[1];
            Picasso
                    .with(ctx)
                    .load(url)
                    .networkPolicy(networkPolicy)
                    .into(img);

            Picasso
                    .with(ctx)
                    .load(R.drawable.img)
                    .memoryPolicy(memoryPolicy)
                    .into(img);

            /*
            * different results for cache/no cache:
            *   cache:
            *   2018-11-17 13:30:45.591 4183-4183/com.example.bb.picassoapp D/Picasso: Main        completed    [R0]+1488ms from DISK
            *   no cache:
            *   2018-11-17 13:31:31.441 4400-4400/com.example.bb.picassoapp D/Picasso: Main        completed    [R0]+1822ms from NETWORK
            * */
        }

        // 7. placeholder
        if (option == 7) {
            Picasso
                    .with(ctx)
                    .load(url)
                    .placeholder(R.drawable.loading)
                    .into(img);
        }

        // 8. error
        if (option == 8) {
            Picasso
                    .with(ctx)
                    .load("fskjbfkbfkebfewkbfw")
                    .error(R.drawable.error)
                    .into(img);
        }

        // 9. callback
        if (option == 9) {
            final Logger logger = Logger.getLogger(this.getClass().getName());
            Picasso
                    .with(ctx)
                    .load(url)
                    .into(img, new Callback() {
                        @Override
                        public void onSuccess() {
                            logger.log(Level.INFO, "loading image success");
                        }

                        @Override
                        public void onError() {
                            logger.log(Level.INFO, "loading image error");
                        }
                    });
        }

        // 10. resize/rotate
        if (option == 10) {

            // default size is 200dp x 200dp

            final int innerOption = 3;

            // just resize so the image stretches
            if (innerOption == 1) {
                Picasso
                        .with(ctx)
                        .load(url)
                        .resize(150, 220)
                        .into(img);
            }
            // use centerCrop() or centerInside()
            if (innerOption == 2) {
                Picasso
                        .with(ctx)
                        .load(url)
                        .resize(150, 220)
                        //.centerCrop()
                        .centerInside()
                        .into(img);
            }
            // use fit method
            if (innerOption == 3) {
                Picasso
                        .with(ctx)
                        .load(url)
                        .fit()
                        .into(img);
            }

        }

        // 11. no fade
        if (option == 11) {
            Picasso
                    .with(ctx)
                    .load(url)
                    .noFade()
                    .into(img);
        }

        // no placeholder
        if (option == 12) {
            Picasso
                    .with(ctx)
                    .load(url)
                    .into(img);

            new Handler().postDelayed(new Runnable() {
                @Override
                public void run() {
                    Picasso
                            .with(ctx)
                            .load(url2)
                            .noPlaceholder()
                            .into(img);
                }
            }, 2000);
        }

        // managing requests
        if (option == 13) {
            final String tag = "imgtag";

            Picasso
                    .with(ctx)
                    .load(url)
                    .tag(tag)
                    .into(img);


            Picasso.with(ctx).pauseTag(tag);
            new Handler().postDelayed(new Runnable() {
                @Override
                public void run() {
                    Picasso.with(ctx).resumeTag(tag);
                    //Picasso.with(ctx).cancelTag(tag);
                }
            }, 2000);
        }

    }
}
